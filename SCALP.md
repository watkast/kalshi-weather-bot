# Range-Scalp Bot

*Updated Sat Oct 31 06:33 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 41890 | 36548 | 5342 (54) | 3 | $-11783.90 | -4.5% |
| **+10¢** | 31224 | 25039 | 6185 (78) | 5 | $-10554.76 | -5.4% |
| **+15¢** | 26102 | 19433 | 6669 (106) | 7 | $-9652.51 | -5.9% |
| **+20¢** | 23179 | 16196 | 6983 (137) | 7 | $-8498.37 | -5.8% |
| **+10¢ (15¢ stop)** | 51070 | 50995 | 75 (41) | 4 | $-19280.62 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-31 06:31 | +10 stop | ZEC | DOWN | 0.67 | 0.77 | 0.72 |
| 10-31 06:31 | +20 | ZEC | DOWN | 0.67 | open |  |
| 10-31 06:31 | +15 | ZEC | DOWN | 0.67 | open |  |
| 10-31 06:31 | +10 | ZEC | DOWN | 0.67 | 0.77 | 0.72 |
| 10-31 06:31 | +5 | ZEC | DOWN | 0.67 | 0.77 | 0.73 |
| 10-31 06:31 | +10 stop | NEAR | DOWN | 0.68 | open |  |
| 10-31 06:31 | +20 | NEAR | DOWN | 0.68 | open |  |
| 10-31 06:31 | +15 | NEAR | DOWN | 0.68 | open |  |
| 10-31 06:31 | +10 | NEAR | DOWN | 0.68 | open |  |
| 10-31 06:31 | +5 | NEAR | DOWN | 0.68 | 0.73 | 0.20 |
| 10-31 06:31 | +10 stop | DOGE | DOWN | 0.68 | open |  |
| 10-31 06:31 | +20 | DOGE | DOWN | 0.68 | open |  |
| 10-31 06:31 | +15 | DOGE | DOWN | 0.68 | open |  |
| 10-31 06:31 | +10 | DOGE | DOWN | 0.68 | open |  |
| 10-31 06:31 | +5 | DOGE | DOWN | 0.68 | 0.73 | 0.20 |
| 10-31 06:31 | +10 stop | ETH | DOWN | 0.65 | open |  |
| 10-31 06:31 | +20 | ETH | DOWN | 0.65 | open |  |
| 10-31 06:31 | +15 | ETH | DOWN | 0.65 | open |  |
| 10-31 06:31 | +10 | ETH | DOWN | 0.65 | open |  |
| 10-31 06:31 | +5 | ETH | DOWN | 0.65 | open |  |
| 10-31 06:31 | +10 stop | HYPE | DOWN | 0.60 | 0.40 | -2.34 |
| 10-31 06:31 | +20 | HYPE | DOWN | 0.60 | open |  |
| 10-31 06:31 | +15 | HYPE | DOWN | 0.60 | open |  |
| 10-31 06:31 | +10 | HYPE | DOWN | 0.60 | open |  |
| 10-31 06:31 | +5 | HYPE | DOWN | 0.60 | open |  |
| 10-31 06:31 | +10 stop | BTC | DOWN | 0.57 | open |  |
| 10-31 06:31 | +20 | BTC | DOWN | 0.57 | open |  |
| 10-31 06:31 | +15 | BTC | DOWN | 0.57 | open |  |
| 10-31 06:31 | +10 | BTC | DOWN | 0.57 | open |  |
| 10-31 06:31 | +5 | BTC | DOWN | 0.57 | open |  |
| 10-31 06:31 | +10 stop | SOL | DOWN | 0.65 | 0.76 | 0.81 |
| 10-31 06:31 | +20 | SOL | DOWN | 0.65 | open |  |
| 10-31 06:31 | +15 | SOL | DOWN | 0.65 | open |  |
| 10-31 06:31 | +10 | SOL | DOWN | 0.65 | 0.76 | 0.81 |
| 10-31 06:31 | +5 | SOL | DOWN | 0.65 | 0.72 | 0.39 |
| 10-31 06:28 | +10 stop | XRP | UP | 0.48 | 0.14 | -3.67 |
| 10-31 06:28 | +10 stop | SOL | DOWN | 0.56 | 0.96 | 3.80 |
| 10-31 06:26 | +10 stop | HYPE | UP | 0.67 | 0.88 | 1.81 |
| 10-31 06:26 | +10 stop | SOL | UP | 0.55 | 0.36 | -2.25 |
| 10-31 06:26 | +10 stop | XRP | UP | 0.61 | 0.45 | -1.95 |
