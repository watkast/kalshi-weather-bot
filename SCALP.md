# Range-Scalp Bot

*Updated Mon Nov 09 05:26 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 53350 | 46514 | 6836 (85) | 0 | $-14760.94 | -4.4% |
| **+10¢** | 39848 | 31874 | 7974 (110) | 0 | $-13765.26 | -5.5% |
| **+15¢** | 33391 | 24799 | 8592 (141) | 0 | $-12569.84 | -6.0% |
| **+20¢** | 29711 | 20703 | 9008 (186) | 1 | $-11058.82 | -5.9% |
| **+10¢ (15¢ stop)** | 65015 | 64909 | 106 (63) | 0 | $-24135.54 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-09 05:22 | +10 stop | ZEC | DOWN | 0.69 | 0.80 | 0.83 |
| 11-09 05:21 | +10 stop | BTC | DOWN | 0.64 | 0.76 | 0.90 |
| 11-09 05:21 | +10 | BTC | DOWN | 0.64 | 0.76 | 0.90 |
| 11-09 05:21 | +5 | BTC | DOWN | 0.64 | 0.73 | 0.59 |
| 11-09 05:21 | +10 stop | XRP | DOWN | 0.67 | 0.81 | 1.13 |
| 11-09 05:21 | +20 | XRP | DOWN | 0.67 | open |  |
| 11-09 05:21 | +15 | XRP | DOWN | 0.67 | 0.84 | 1.44 |
| 11-09 05:21 | +10 | XRP | DOWN | 0.67 | 0.81 | 1.13 |
| 11-09 05:21 | +5 | XRP | DOWN | 0.67 | 0.72 | 0.19 |
| 11-09 05:18 | +5 | SOL | DOWN | 0.69 | 0.75 | 0.31 |
| 11-09 05:17 | +10 stop | SOL | DOWN | 0.69 | 0.79 | 0.73 |
| 11-09 05:17 | +20 | SOL | DOWN | 0.69 | 0.91 | 2.03 |
| 11-09 05:17 | +15 | SOL | DOWN | 0.69 | 0.84 | 1.25 |
| 11-09 05:17 | +10 | SOL | DOWN | 0.68 | 0.79 | 0.82 |
| 11-09 05:17 | +5 | SOL | DOWN | 0.68 | 0.73 | 0.20 |
| 11-09 05:17 | +10 stop | NEAR | DOWN | 0.69 | 0.81 | 0.94 |
| 11-09 05:17 | +20 | NEAR | DOWN | 0.69 | 0.91 | 1.96 |
| 11-09 05:17 | +15 | NEAR | DOWN | 0.69 | 0.88 | 1.67 |
| 11-09 05:17 | +10 | NEAR | DOWN | 0.69 | 0.81 | 0.94 |
| 11-09 05:17 | +5 | NEAR | DOWN | 0.69 | 0.76 | 0.42 |
| 11-09 05:16 | +10 stop | HYPE | DOWN | 0.57 | 0.67 | 0.66 |
| 11-09 05:16 | +20 | HYPE | DOWN | 0.57 | 0.87 | 2.74 |
| 11-09 05:16 | +15 | HYPE | DOWN | 0.56 | 0.71 | 1.17 |
| 11-09 05:16 | +10 | HYPE | DOWN | 0.56 | 0.67 | 0.76 |
| 11-09 05:16 | +5 | HYPE | DOWN | 0.57 | 0.67 | 0.63 |
| 11-09 05:16 | +10 stop | BTC | DOWN | 0.68 | 0.81 | 1.03 |
| 11-09 05:16 | +20 | BTC | DOWN | 0.69 | 0.90 | 1.91 |
| 11-09 05:16 | +15 | BTC | DOWN | 0.69 | 0.85 | 1.36 |
| 11-09 05:16 | +10 | BTC | DOWN | 0.69 | 0.81 | 0.94 |
| 11-09 05:16 | +5 | BTC | DOWN | 0.69 | 0.75 | 0.31 |
| 11-09 05:15 | +10 stop | ZEC | DOWN | 0.66 | 0.48 | -2.14 |
| 11-09 05:15 | +20 | ZEC | DOWN | 0.66 | 0.89 | 2.07 |
| 11-09 05:15 | +15 | ZEC | DOWN | 0.66 | 0.81 | 1.23 |
| 11-09 05:15 | +10 | ZEC | DOWN | 0.66 | 0.80 | 1.12 |
| 11-09 05:15 | +5 | ZEC | DOWN | 0.66 | 0.75 | 0.60 |
| 11-09 05:12 | +10 stop | DOGE | UP | 0.49 | 0.13 | -3.86 |
| 11-09 05:12 | +20 | DOGE | UP | 0.49 | no | -5.08 |
| 11-09 05:12 | +15 | DOGE | UP | 0.49 | no | -5.08 |
| 11-09 05:12 | +10 | DOGE | UP | 0.49 | no | -5.08 |
| 11-09 05:12 | +5 | DOGE | UP | 0.49 | 0.55 | 0.24 |
