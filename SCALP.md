# Range-Scalp Bot

*Updated Mon Nov 09 00:24 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 53031 | 46244 | 6787 (85) | 2 | $-14621.72 | -4.4% |
| **+10¢** | 39586 | 31672 | 7914 (110) | 3 | $-13611.39 | -5.5% |
| **+15¢** | 33170 | 24644 | 8526 (141) | 3 | $-12412.76 | -6.0% |
| **+20¢** | 29503 | 20562 | 8941 (186) | 4 | $-10941.08 | -5.9% |
| **+10¢ (15¢ stop)** | 64568 | 64462 | 106 (63) | 0 | $-23911.97 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-09 00:23 | +10 stop | HYPE | DOWN | 0.63 | 0.74 | 0.79 |
| 11-09 00:23 | +20 | HYPE | DOWN | 0.63 | open |  |
| 11-09 00:23 | +15 | HYPE | DOWN | 0.63 | open |  |
| 11-09 00:23 | +10 | HYPE | DOWN | 0.63 | 0.74 | 0.79 |
| 11-09 00:23 | +5 | HYPE | DOWN | 0.63 | 0.74 | 0.79 |
| 11-09 00:22 | +5 | BNB | UP | 0.66 | 0.83 | 1.44 |
| 11-09 00:22 | +10 stop | BNB | UP | 0.66 | 0.83 | 1.44 |
| 11-09 00:22 | +10 stop | ZEC | UP | 0.49 | 0.62 | 0.95 |
| 11-09 00:22 | +15 | ZEC | UP | 0.49 | 0.70 | 1.77 |
| 11-09 00:22 | +10 | ZEC | UP | 0.49 | 0.62 | 0.95 |
| 11-09 00:22 | +5 | ZEC | UP | 0.50 | 0.62 | 0.85 |
| 11-09 00:22 | +10 stop | SOL | DOWN | 0.55 | 0.31 | -2.73 |
| 11-09 00:22 | +5 | SOL | DOWN | 0.55 | open |  |
| 11-09 00:22 | +10 stop | NEAR | DOWN | 0.56 | 0.68 | 0.86 |
| 11-09 00:22 | +5 | ETH | DOWN | 0.48 | 0.65 | 1.36 |
| 11-09 00:22 | +10 stop | ZEC | DOWN | 0.52 | 0.69 | 1.37 |
| 11-09 00:22 | +15 | ZEC | DOWN | 0.52 | 0.69 | 1.41 |
| 11-09 00:22 | +10 | ZEC | DOWN | 0.51 | 0.69 | 1.47 |
| 11-09 00:22 | +5 | ZEC | DOWN | 0.50 | 0.69 | 1.57 |
| 11-09 00:21 | +10 stop | BTC | DOWN | 0.59 | 0.28 | -3.42 |
| 11-09 00:20 | +10 stop | BNB | DOWN | 0.65 | 0.76 | 0.81 |
| 11-09 00:20 | +10 stop | XRP | DOWN | 0.71 | 0.49 | -2.53 |
| 11-09 00:20 | +10 | XRP | DOWN | 0.71 | open |  |
| 11-09 00:20 | +5 | XRP | DOWN | 0.70 | 0.79 | 0.63 |
| 11-09 00:20 | +10 stop | ETH | DOWN | 0.67 | 0.48 | -2.24 |
| 11-09 00:20 | +10 stop | ZEC | DOWN | 0.69 | 0.81 | 0.94 |
| 11-09 00:19 | +5 | BNB | UP | 0.56 | 0.66 | 0.71 |
| 11-09 00:19 | +10 stop | XRP | DOWN | 0.55 | 0.66 | 0.76 |
| 11-09 00:19 | +20 | XRP | DOWN | 0.55 | 0.79 | 2.10 |
| 11-09 00:19 | +15 | XRP | DOWN | 0.55 | 0.71 | 1.27 |
| 11-09 00:19 | +10 | XRP | DOWN | 0.55 | 0.66 | 0.76 |
| 11-09 00:19 | +5 | XRP | DOWN | 0.56 | 0.64 | 0.45 |
| 11-09 00:19 | +10 stop | BTC | UP | 0.71 | 0.53 | -2.13 |
| 11-09 00:19 | +20 | BTC | UP | 0.71 | 0.91 | 1.80 |
| 11-09 00:19 | +15 | BTC | UP | 0.71 | 0.91 | 1.80 |
| 11-09 00:19 | +10 | BTC | UP | 0.71 | 0.81 | 0.74 |
| 11-09 00:19 | +5 | BTC | UP | 0.70 | 0.79 | 0.63 |
| 11-09 00:19 | +10 stop | DOGE | DOWN | 0.62 | 0.77 | 1.20 |
| 11-09 00:19 | +20 | DOGE | DOWN | 0.62 | 0.84 | 1.93 |
| 11-09 00:19 | +15 | DOGE | DOWN | 0.63 | 0.80 | 1.41 |
