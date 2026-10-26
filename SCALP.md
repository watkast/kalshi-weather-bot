# Range-Scalp Bot

*Updated Mon Oct 26 16:29 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 35103 | 30646 | 4457 (43) | 0 | $-9747.69 | -4.4% |
| **+10¢** | 26268 | 21115 | 5153 (65) | 0 | $-8545.28 | -5.2% |
| **+15¢** | 21976 | 16428 | 5548 (89) | 0 | $-7657.08 | -5.5% |
| **+20¢** | 19482 | 13667 | 5815 (112) | 0 | $-6726.82 | -5.5% |
| **+10¢ (15¢ stop)** | 42975 | 42913 | 62 (33) | 0 | $-16279.49 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-26 16:26 | +10 stop | HYPE | UP | 0.26 | 0.55 | 2.58 |
| 10-26 16:26 | +10 stop | SOL | DOWN | 0.69 | 0.84 | 1.25 |
| 10-26 16:24 | +10 stop | ETH | UP | 0.61 | 0.43 | -2.15 |
| 10-26 16:24 | +10 stop | SOL | UP | 0.62 | 0.40 | -2.54 |
| 10-26 16:24 | +10 stop | BNB | UP | 0.69 | 0.50 | -2.23 |
| 10-26 16:24 | +10 stop | BTC | DOWN | 0.63 | 0.78 | 1.20 |
| 10-26 16:24 | +10 | BTC | DOWN | 0.63 | 0.78 | 1.20 |
| 10-26 16:24 | +5 | BTC | DOWN | 0.63 | 0.78 | 1.20 |
| 10-26 16:23 | +10 stop | HYPE | DOWN | 0.64 | 0.49 | -1.85 |
| 10-26 16:23 | +10 | HYPE | DOWN | 0.64 | 0.78 | 1.10 |
| 10-26 16:23 | +5 | HYPE | DOWN | 0.64 | 0.73 | 0.59 |
| 10-26 16:23 | +10 stop | BNB | DOWN | 0.61 | 0.34 | -3.03 |
| 10-26 16:23 | +10 stop | SOL | DOWN | 0.65 | 0.38 | -3.03 |
| 10-26 16:23 | +5 | SOL | DOWN | 0.65 | 0.78 | 1.01 |
| 10-26 16:22 | +10 stop | BTC | DOWN | 0.66 | 0.78 | 0.91 |
| 10-26 16:22 | +5 | BTC | DOWN | 0.66 | 0.75 | 0.60 |
| 10-26 16:22 | +10 stop | XRP | DOWN | 0.68 | 0.52 | -1.94 |
| 10-26 16:22 | +20 | XRP | DOWN | 0.68 | 0.89 | 1.87 |
| 10-26 16:22 | +15 | XRP | DOWN | 0.68 | 0.85 | 1.45 |
| 10-26 16:22 | +10 | XRP | DOWN | 0.68 | 0.80 | 0.92 |
| 10-26 16:22 | +5 | XRP | DOWN | 0.68 | 0.76 | 0.51 |
| 10-26 16:22 | +10 stop | HYPE | DOWN | 0.42 | 0.63 | 1.75 |
| 10-26 16:22 | +10 | HYPE | DOWN | 0.42 | 0.63 | 1.75 |
| 10-26 16:22 | +5 | HYPE | DOWN | 0.45 | 0.63 | 1.45 |
| 10-26 16:21 | +5 | BTC | DOWN | 0.64 | 0.71 | 0.38 |
| 10-26 16:21 | +5 | SOL | DOWN | 0.54 | 0.62 | 0.45 |
| 10-26 16:21 | +10 stop | HYPE | DOWN | 0.53 | 0.63 | 0.65 |
| 10-26 16:21 | +20 | HYPE | DOWN | 0.53 | 0.73 | 1.68 |
| 10-26 16:21 | +15 | HYPE | DOWN | 0.53 | 0.73 | 1.68 |
| 10-26 16:21 | +10 | HYPE | DOWN | 0.53 | 0.63 | 0.65 |
| 10-26 16:21 | +5 | HYPE | DOWN | 0.53 | 0.62 | 0.55 |
| 10-26 16:21 | +10 stop | BTC | DOWN | 0.59 | 0.71 | 0.88 |
| 10-26 16:20 | +5 | SOL | DOWN | 0.59 | 0.64 | 0.16 |
| 10-26 16:20 | +10 stop | BNB | DOWN | 0.59 | 0.41 | -2.14 |
| 10-26 16:20 | +5 | BTC | DOWN | 0.59 | 0.67 | 0.47 |
| 10-26 16:19 | +5 | BTC | DOWN | 0.54 | 0.60 | 0.25 |
| 10-26 16:19 | +5 | SOL | DOWN | 0.60 | 0.70 | 0.68 |
| 10-26 16:19 | +10 stop | ETH | DOWN | 0.61 | 0.42 | -2.25 |
| 10-26 16:19 | +20 | ETH | DOWN | 0.61 | 0.83 | 1.93 |
| 10-26 16:19 | +15 | ETH | DOWN | 0.61 | 0.83 | 1.93 |
