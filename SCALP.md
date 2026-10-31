# Range-Scalp Bot

*Updated Sat Oct 31 04:20 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 41752 | 36432 | 5320 (54) | 8 | $-11712.86 | -4.5% |
| **+10¢** | 31118 | 24961 | 6157 (78) | 9 | $-10464.27 | -5.3% |
| **+15¢** | 26008 | 19369 | 6639 (106) | 9 | $-9564.33 | -5.9% |
| **+20¢** | 23091 | 16138 | 6953 (137) | 9 | $-8430.31 | -5.8% |
| **+10¢ (15¢ stop)** | 50903 | 50828 | 75 (41) | 2 | $-19222.14 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-31 04:20 | +5 | HYPE | UP | 0.65 | open |  |
| 10-31 04:19 | +10 stop | BNB | UP | 0.67 | open |  |
| 10-31 04:17 | +10 stop | ETH | UP | 0.65 | 0.77 | 0.91 |
| 10-31 04:17 | +10 stop | HYPE | UP | 0.64 | open |  |
| 10-31 04:17 | +5 | HYPE | UP | 0.64 | 0.71 | 0.38 |
| 10-31 04:17 | +10 stop | ZEC | UP | 0.70 | 0.80 | 0.73 |
| 10-31 04:17 | +10 stop | DOGE | UP | 0.60 | 0.73 | 0.99 |
| 10-31 04:17 | +10 stop | NEAR | UP | 0.70 | 0.80 | 0.73 |
| 10-31 04:17 | +10 stop | BNB | UP | 0.53 | 0.63 | 0.65 |
| 10-31 04:17 | +10 stop | SOL | UP | 0.69 | 0.79 | 0.73 |
| 10-31 04:17 | +10 stop | BTC | UP | 0.59 | 0.78 | 1.60 |
| 10-31 04:17 | +5 | SOL | UP | 0.70 | 0.79 | 0.63 |
| 10-31 04:16 | +10 stop | HYPE | DOWN | 0.45 | 0.25 | -2.32 |
| 10-31 04:16 | +20 | HYPE | DOWN | 0.45 | open |  |
| 10-31 04:16 | +15 | HYPE | DOWN | 0.45 | open |  |
| 10-31 04:16 | +10 | HYPE | DOWN | 0.45 | open |  |
| 10-31 04:16 | +5 | HYPE | DOWN | 0.45 | 0.54 | 0.54 |
| 10-31 04:16 | +10 stop | ETH | DOWN | 0.68 | 0.49 | -2.24 |
| 10-31 04:16 | +20 | ETH | DOWN | 0.68 | open |  |
| 10-31 04:16 | +15 | ETH | DOWN | 0.68 | open |  |
| 10-31 04:16 | +10 | ETH | DOWN | 0.68 | open |  |
| 10-31 04:16 | +5 | ETH | DOWN | 0.68 | open |  |
| 10-31 04:16 | +10 stop | ZEC | DOWN | 0.59 | 0.35 | -2.73 |
| 10-31 04:16 | +20 | ZEC | DOWN | 0.59 | open |  |
| 10-31 04:16 | +15 | ZEC | DOWN | 0.59 | open |  |
| 10-31 04:16 | +10 | ZEC | DOWN | 0.59 | open |  |
| 10-31 04:16 | +5 | ZEC | DOWN | 0.59 | open |  |
| 10-31 04:16 | +10 stop | DOGE | DOWN | 0.57 | 0.42 | -1.86 |
| 10-31 04:16 | +20 | DOGE | DOWN | 0.57 | open |  |
| 10-31 04:16 | +15 | DOGE | DOWN | 0.57 | open |  |
| 10-31 04:16 | +10 | DOGE | DOWN | 0.57 | open |  |
| 10-31 04:16 | +5 | DOGE | DOWN | 0.57 | open |  |
| 10-31 04:16 | +10 stop | NEAR | DOWN | 0.56 | 0.38 | -2.15 |
| 10-31 04:16 | +20 | NEAR | DOWN | 0.56 | open |  |
| 10-31 04:16 | +15 | NEAR | DOWN | 0.56 | open |  |
| 10-31 04:16 | +10 | NEAR | DOWN | 0.56 | open |  |
| 10-31 04:16 | +5 | NEAR | DOWN | 0.56 | open |  |
| 10-31 04:16 | +10 stop | SOL | DOWN | 0.54 | 0.39 | -1.85 |
| 10-31 04:16 | +20 | SOL | DOWN | 0.54 | open |  |
| 10-31 04:16 | +15 | SOL | DOWN | 0.54 | open |  |
