# Range-Scalp Bot

*Updated Wed Oct 21 13:31 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 27283 | 23758 | 3525 (39) | 0 | $-7938.53 | -4.6% |
| **+10¢** | 20507 | 16434 | 4073 (55) | 0 | $-7019.80 | -5.4% |
| **+15¢** | 17172 | 12789 | 4383 (78) | 0 | $-6280.90 | -5.8% |
| **+20¢** | 15201 | 10607 | 4594 (98) | 0 | $-5647.28 | -5.9% |
| **+10¢ (15¢ stop)** | 33484 | 33425 | 59 (32) | 0 | $-12418.24 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-21 13:28 | +10 stop | XRP | UP | 0.52 | 0.63 | 0.75 |
| 10-21 13:28 | +20 | XRP | UP | 0.55 | no | -5.68 |
| 10-21 13:28 | +15 | XRP | UP | 0.52 | no | -5.38 |
| 10-21 13:28 | +10 | XRP | UP | 0.52 | 0.63 | 0.75 |
| 10-21 13:28 | +5 | XRP | UP | 0.50 | 0.63 | 0.95 |
| 10-21 13:26 | +10 stop | DOGE | DOWN | 0.42 | 0.52 | 0.64 |
| 10-21 13:26 | +10 stop | BTC | DOWN | 0.60 | 0.77 | 1.40 |
| 10-21 13:26 | +10 stop | DOGE | DOWN | 0.37 | 0.61 | 2.06 |
| 10-21 13:26 | +10 stop | SOL | DOWN | 0.71 | 0.81 | 0.74 |
| 10-21 13:24 | +10 stop | ZEC | UP | 0.69 | 0.80 | 0.81 |
| 10-21 13:24 | +20 | ZEC | UP | 0.68 | 0.91 | 2.06 |
| 10-21 13:24 | +15 | ZEC | UP | 0.68 | 0.86 | 1.52 |
| 10-21 13:24 | +10 | ZEC | UP | 0.68 | 0.80 | 0.90 |
| 10-21 13:24 | +5 | ZEC | UP | 0.69 | 0.80 | 0.83 |
| 10-21 13:24 | +10 stop | HYPE | DOWN | 0.67 | 0.77 | 0.71 |
| 10-21 13:24 | +5 | HYPE | DOWN | 0.70 | 0.77 | 0.42 |
| 10-21 13:24 | +10 stop | NEAR | DOWN | 0.71 | 0.87 | 1.37 |
| 10-21 13:24 | +10 stop | BNB | DOWN | 0.70 | 0.81 | 0.84 |
| 10-21 13:23 | +10 stop | DOGE | DOWN | 0.64 | 0.75 | 0.79 |
| 10-21 13:23 | +10 stop | XRP | UP | 0.63 | 0.73 | 0.69 |
| 10-21 13:23 | +5 | HYPE | UP | 0.52 | 0.62 | 0.65 |
| 10-21 13:23 | +10 stop | NEAR | UP | 0.54 | 0.37 | -2.05 |
| 10-21 13:23 | +5 | NEAR | UP | 0.54 | no | -5.58 |
| 10-21 13:22 | +5 | DOGE | UP | 0.62 | no | -6.37 |
| 10-21 13:22 | +10 stop | XRP | UP | 0.56 | 0.66 | 0.66 |
| 10-21 13:21 | +10 stop | BTC | DOWN | 0.58 | 0.77 | 1.59 |
| 10-21 13:21 | +10 stop | BNB | DOWN | 0.63 | 0.44 | -2.25 |
| 10-21 13:21 | +10 stop | DOGE | UP | 0.59 | 0.40 | -2.24 |
| 10-21 13:21 | +15 | DOGE | UP | 0.59 | no | -6.07 |
| 10-21 13:21 | +10 | DOGE | UP | 0.59 | no | -6.07 |
| 10-21 13:21 | +5 | DOGE | UP | 0.59 | 0.65 | 0.27 |
| 10-21 13:21 | +10 stop | ETH | DOWN | 0.68 | 0.78 | 0.71 |
| 10-21 13:20 | +5 | HYPE | UP | 0.63 | 0.68 | 0.17 |
| 10-21 13:20 | +10 stop | NEAR | DOWN | 0.63 | 0.45 | -2.15 |
| 10-21 13:20 | +5 | NEAR | DOWN | 0.63 | 0.68 | 0.17 |
| 10-21 13:20 | +10 stop | XRP | UP | 0.69 | 0.53 | -1.93 |
| 10-21 13:20 | +5 | DOGE | UP | 0.68 | 0.75 | 0.40 |
| 10-21 13:19 | +10 stop | HYPE | UP | 0.59 | 0.41 | -2.14 |
| 10-21 13:19 | +5 | HYPE | UP | 0.59 | 0.67 | 0.47 |
| 10-21 13:19 | +10 stop | HYPE | DOWN | 0.40 | 0.57 | 1.31 |
