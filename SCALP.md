# Range-Scalp Bot

*Updated Sat Oct 31 07:31 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 41955 | 36605 | 5350 (54) | 0 | $-11793.95 | -4.5% |
| **+10¢** | 31276 | 25081 | 6195 (78) | 0 | $-10563.09 | -5.4% |
| **+15¢** | 26145 | 19466 | 6679 (106) | 0 | $-9657.22 | -5.9% |
| **+20¢** | 23217 | 16223 | 6994 (137) | 0 | $-8506.17 | -5.8% |
| **+10¢ (15¢ stop)** | 51143 | 51068 | 75 (41) | 0 | $-19287.65 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-31 07:27 | +10 stop | DOGE | DOWN | 0.70 | 0.84 | 1.15 |
| 10-31 07:26 | +10 stop | BTC | UP | 0.58 | 0.94 | 3.35 |
| 10-31 07:25 | +10 stop | DOGE | DOWN | 0.57 | 0.67 | 0.68 |
| 10-31 07:24 | +10 stop | BNB | DOWN | 0.65 | 0.35 | -3.32 |
| 10-31 07:24 | +10 stop | DOGE | DOWN | 0.61 | 0.43 | -2.15 |
| 10-31 07:23 | +10 stop | BTC | DOWN | 0.69 | 0.42 | -3.03 |
| 10-31 07:22 | +10 stop | ETH | UP | 0.64 | 0.80 | 1.31 |
| 10-31 07:22 | +10 | ETH | UP | 0.64 | 0.80 | 1.31 |
| 10-31 07:22 | +5 | ETH | UP | 0.64 | 0.72 | 0.48 |
| 10-31 07:22 | +10 stop | DOGE | DOWN | 0.59 | 0.69 | 0.68 |
| 10-31 07:22 | +10 stop | HYPE | UP | 0.70 | 0.84 | 1.11 |
| 10-31 07:22 | +20 | HYPE | UP | 0.70 | 0.93 | 2.07 |
| 10-31 07:22 | +15 | HYPE | UP | 0.70 | 0.87 | 1.43 |
| 10-31 07:22 | +10 | HYPE | UP | 0.69 | 0.84 | 1.21 |
| 10-31 07:22 | +5 | HYPE | UP | 0.68 | 0.74 | 0.26 |
| 10-31 07:21 | +10 stop | DOGE | DOWN | 0.52 | 0.64 | 0.85 |
| 10-31 07:19 | +10 stop | DOGE | UP | 0.67 | 0.34 | -3.62 |
| 10-31 07:19 | +10 | DOGE | UP | 0.67 | no | -6.86 |
| 10-31 07:19 | +5 | DOGE | UP | 0.68 | no | -6.96 |
| 10-31 07:19 | +10 stop | NEAR | UP | 0.65 | 0.46 | -2.23 |
| 10-31 07:19 | +15 | NEAR | UP | 0.65 | no | -6.64 |
| 10-31 07:19 | +10 | NEAR | UP | 0.65 | no | -6.64 |
| 10-31 07:18 | +10 stop | BNB | DOWN | 0.61 | 0.76 | 1.16 |
| 10-31 07:18 | +5 | NEAR | UP | 0.70 | no | -7.15 |
| 10-31 07:18 | +10 stop | BTC | UP | 0.63 | 0.37 | -2.94 |
| 10-31 07:18 | +10 | BTC | UP | 0.63 | 0.94 | 2.86 |
| 10-31 07:17 | +5 | BTC | UP | 0.66 | 0.94 | 2.57 |
| 10-31 07:16 | +10 stop | BNB | UP | 0.59 | 0.42 | -2.04 |
| 10-31 07:16 | +20 | BNB | UP | 0.58 | 0.85 | 2.39 |
| 10-31 07:16 | +15 | BNB | UP | 0.58 | 0.75 | 1.34 |
| 10-31 07:16 | +10 | BNB | UP | 0.59 | 0.75 | 1.29 |
| 10-31 07:16 | +5 | BNB | UP | 0.58 | 0.64 | 0.21 |
| 10-31 07:16 | +10 stop | ZEC | UP | 0.68 | 0.85 | 1.45 |
| 10-31 07:16 | +20 | ZEC | UP | 0.68 | 0.89 | 1.87 |
| 10-31 07:16 | +15 | ZEC | UP | 0.68 | 0.85 | 1.45 |
| 10-31 07:16 | +10 | ZEC | UP | 0.68 | 0.85 | 1.45 |
| 10-31 07:16 | +5 | ZEC | UP | 0.68 | 0.85 | 1.45 |
| 10-31 07:16 | +10 stop | ETH | UP | 0.69 | 0.81 | 0.94 |
| 10-31 07:16 | +20 | ETH | UP | 0.69 | 0.92 | 2.06 |
| 10-31 07:16 | +15 | ETH | UP | 0.69 | 0.92 | 2.09 |
