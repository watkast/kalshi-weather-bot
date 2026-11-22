# Range-Scalp Bot

*Updated Sun Nov 22 22:31 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 69175 | 60356 | 8819 (145) | 1 | $-18646.49 | -4.3% |
| **+10¢** | 51622 | 41326 | 10296 (188) | 3 | $-17293.38 | -5.3% |
| **+15¢** | 43265 | 32167 | 11098 (241) | 2 | $-15502.49 | -5.7% |
| **+20¢** | 38531 | 26868 | 11663 (300) | 3 | $-13788.15 | -5.7% |
| **+10¢ (15¢ stop)** | 84243 | 84054 | 189 (117) | 3 | $-31042.61 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-22 22:31 | +10 stop | BTC | UP | 0.51 | open |  |
| 11-22 22:31 | +20 | BTC | UP | 0.51 | open |  |
| 11-22 22:31 | +15 | BTC | UP | 0.51 | open |  |
| 11-22 22:31 | +10 | BTC | UP | 0.51 | open |  |
| 11-22 22:31 | +5 | BTC | UP | 0.51 | 0.59 | 0.45 |
| 11-22 22:31 | +10 stop | HYPE | DOWN | 0.69 | open |  |
| 11-22 22:31 | +20 | HYPE | DOWN | 0.69 | open |  |
| 11-22 22:31 | +15 | HYPE | DOWN | 0.69 | open |  |
| 11-22 22:31 | +10 | HYPE | DOWN | 0.69 | open |  |
| 11-22 22:31 | +5 | HYPE | DOWN | 0.70 | open |  |
| 11-22 22:31 | +10 stop | ZEC | DOWN | 0.71 | open |  |
| 11-22 22:31 | +20 | ZEC | DOWN | 0.71 | open |  |
| 11-22 22:31 | +10 | ZEC | DOWN | 0.70 | open |  |
| 11-22 22:31 | +5 | ZEC | DOWN | 0.70 | 0.76 | 0.32 |
| 11-22 22:20 | +10 stop | ETH | DOWN | 0.62 | 0.77 | 1.21 |
| 11-22 22:20 | +10 stop | BTC | DOWN | 0.58 | 0.68 | 0.66 |
| 11-22 22:20 | +10 stop | BNB | DOWN | 0.62 | 0.72 | 0.68 |
| 11-22 22:18 | +10 stop | BNB | DOWN | 0.59 | 0.70 | 0.79 |
| 11-22 22:18 | +5 | XRP | DOWN | 0.67 | 0.79 | 0.92 |
| 11-22 22:18 | +5 | HYPE | DOWN | 0.66 | 0.81 | 1.23 |
| 11-22 22:18 | +10 stop | DOGE | DOWN | 0.59 | 0.73 | 1.09 |
| 11-22 22:18 | +10 | DOGE | DOWN | 0.59 | 0.73 | 1.09 |
| 11-22 22:18 | +5 | DOGE | DOWN | 0.59 | 0.73 | 1.09 |
| 11-22 22:18 | +10 stop | DOGE | UP | 0.46 | 0.59 | 0.95 |
| 11-22 22:18 | +20 | DOGE | UP | 0.47 | no | -4.88 |
| 11-22 22:18 | +15 | DOGE | UP | 0.47 | no | -4.88 |
| 11-22 22:18 | +10 | DOGE | UP | 0.47 | 0.59 | 0.85 |
| 11-22 22:18 | +5 | DOGE | UP | 0.47 | 0.59 | 0.85 |
| 11-22 22:17 | +5 | BTC | UP | 0.60 | no | -6.17 |
| 11-22 22:17 | +10 stop | BNB | UP | 0.63 | 0.40 | -2.64 |
| 11-22 22:17 | +20 | BNB | UP | 0.63 | no | -6.47 |
| 11-22 22:17 | +15 | BNB | UP | 0.63 | no | -6.47 |
| 11-22 22:17 | +10 | BNB | UP | 0.63 | no | -6.47 |
| 11-22 22:17 | +5 | BNB | UP | 0.63 | no | -6.47 |
| 11-22 22:17 | +5 | SOL | DOWN | 0.53 | 0.60 | 0.35 |
| 11-22 22:17 | +10 stop | ETH | UP | 0.68 | 0.37 | -3.43 |
| 11-22 22:17 | +20 | ETH | UP | 0.68 | no | -6.96 |
| 11-22 22:17 | +15 | ETH | UP | 0.68 | no | -6.96 |
| 11-22 22:17 | +10 | ETH | UP | 0.67 | no | -6.86 |
| 11-22 22:17 | +5 | ETH | UP | 0.65 | no | -6.66 |
