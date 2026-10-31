# Range-Scalp Bot

*Updated Sat Oct 31 07:20 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 41949 | 36601 | 5348 (54) | 4 | $-11783.36 | -4.5% |
| **+10¢** | 31270 | 25077 | 6193 (78) | 4 | $-10556.26 | -5.4% |
| **+15¢** | 26139 | 19462 | 6677 (106) | 5 | $-9652.22 | -5.9% |
| **+20¢** | 23209 | 16217 | 6992 (137) | 7 | $-8507.74 | -5.8% |
| **+10¢ (15¢ stop)** | 51132 | 51057 | 75 (41) | 1 | $-19285.34 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-31 07:19 | +10 stop | DOGE | UP | 0.67 | 0.34 | -3.62 |
| 10-31 07:19 | +10 | DOGE | UP | 0.67 | open |  |
| 10-31 07:19 | +5 | DOGE | UP | 0.68 | open |  |
| 10-31 07:19 | +10 stop | NEAR | UP | 0.65 | 0.46 | -2.23 |
| 10-31 07:19 | +15 | NEAR | UP | 0.65 | open |  |
| 10-31 07:19 | +10 | NEAR | UP | 0.65 | open |  |
| 10-31 07:18 | +10 stop | BNB | DOWN | 0.61 | 0.76 | 1.16 |
| 10-31 07:18 | +5 | NEAR | UP | 0.70 | open |  |
| 10-31 07:18 | +10 stop | BTC | UP | 0.63 | open |  |
| 10-31 07:18 | +10 | BTC | UP | 0.63 | open |  |
| 10-31 07:17 | +5 | BTC | UP | 0.66 | open |  |
| 10-31 07:16 | +10 stop | BNB | UP | 0.59 | 0.42 | -2.04 |
| 10-31 07:16 | +20 | BNB | UP | 0.58 | open |  |
| 10-31 07:16 | +15 | BNB | UP | 0.58 | open |  |
| 10-31 07:16 | +10 | BNB | UP | 0.59 | open |  |
| 10-31 07:16 | +5 | BNB | UP | 0.58 | open |  |
| 10-31 07:16 | +10 stop | ZEC | UP | 0.68 | 0.85 | 1.45 |
| 10-31 07:16 | +20 | ZEC | UP | 0.68 | open |  |
| 10-31 07:16 | +15 | ZEC | UP | 0.68 | 0.85 | 1.45 |
| 10-31 07:16 | +10 | ZEC | UP | 0.68 | 0.85 | 1.45 |
| 10-31 07:16 | +5 | ZEC | UP | 0.68 | 0.85 | 1.45 |
| 10-31 07:16 | +10 stop | ETH | UP | 0.69 | 0.81 | 0.94 |
| 10-31 07:16 | +20 | ETH | UP | 0.69 | open |  |
| 10-31 07:16 | +15 | ETH | UP | 0.69 | open |  |
| 10-31 07:16 | +10 | ETH | UP | 0.69 | 0.81 | 0.94 |
| 10-31 07:16 | +5 | ETH | UP | 0.69 | 0.78 | 0.62 |
| 10-31 07:16 | +10 stop | DOGE | UP | 0.64 | 0.76 | 0.90 |
| 10-31 07:16 | +20 | DOGE | UP | 0.64 | open |  |
| 10-31 07:16 | +15 | DOGE | UP | 0.64 | open |  |
| 10-31 07:16 | +10 | DOGE | UP | 0.64 | 0.76 | 0.90 |
| 10-31 07:16 | +5 | DOGE | UP | 0.64 | 0.71 | 0.38 |
| 10-31 07:16 | +10 stop | SOL | UP | 0.65 | 0.76 | 0.81 |
| 10-31 07:16 | +20 | SOL | UP | 0.65 | open |  |
| 10-31 07:16 | +15 | SOL | UP | 0.65 | 0.83 | 1.54 |
| 10-31 07:16 | +10 | SOL | UP | 0.65 | 0.76 | 0.81 |
| 10-31 07:16 | +5 | SOL | UP | 0.65 | 0.76 | 0.81 |
| 10-31 07:16 | +10 stop | BTC | UP | 0.57 | 0.69 | 0.87 |
| 10-31 07:16 | +20 | BTC | UP | 0.57 | open |  |
| 10-31 07:16 | +15 | BTC | UP | 0.58 | open |  |
| 10-31 07:16 | +10 | BTC | UP | 0.58 | 0.69 | 0.77 |
