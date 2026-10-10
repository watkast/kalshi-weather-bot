# Range-Scalp Bot

*Updated Sat Oct 10 01:30 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 9778 | 8439 | 1339 (18) | 0 | $-3292.34 | -5.3% |
| **+10¢** | 7385 | 5820 | 1565 (30) | 0 | $-3188.09 | -6.9% |
| **+15¢** | 6224 | 4574 | 1650 (43) | 1 | $-2654.32 | -6.8% |
| **+20¢** | 5538 | 3822 | 1716 (55) | 1 | $-2225.49 | -6.4% |
| **+10¢ (15¢ stop)** | 11978 | 11943 | 35 (22) | 0 | $-4618.58 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-10 01:28 | +10 stop | SOL | UP | 0.42 | 0.69 | 2.37 |
| 10-10 01:28 | +20 | SOL | UP | 0.43 | 0.69 | 2.27 |
| 10-10 01:28 | +15 | SOL | UP | 0.42 | 0.69 | 2.37 |
| 10-10 01:28 | +10 | SOL | UP | 0.41 | 0.69 | 2.48 |
| 10-10 01:28 | +5 | SOL | UP | 0.41 | 0.69 | 2.48 |
| 10-10 01:27 | +10 stop | BTC | UP | 0.69 | 0.84 | 1.25 |
| 10-10 01:27 | +10 | BTC | UP | 0.69 | 0.84 | 1.25 |
| 10-10 01:27 | +5 | BTC | UP | 0.69 | 0.84 | 1.25 |
| 10-10 01:27 | +10 stop | BNB | DOWN | 0.68 | 0.49 | -2.28 |
| 10-10 01:27 | +20 | BNB | DOWN | 0.68 | 0.97 | 2.67 |
| 10-10 01:27 | +15 | BNB | DOWN | 0.68 | 0.97 | 2.67 |
| 10-10 01:27 | +10 | BNB | DOWN | 0.68 | 0.97 | 2.67 |
| 10-10 01:27 | +5 | BNB | DOWN | 0.68 | 0.97 | 2.67 |
| 10-10 01:27 | +10 stop | XRP | UP | 0.65 | 0.80 | 1.22 |
| 10-10 01:26 | +10 | XRP | UP | 0.65 | 0.80 | 1.22 |
| 10-10 01:26 | +5 | XRP | UP | 0.65 | 0.80 | 1.22 |
| 10-10 01:26 | +10 stop | BTC | DOWN | 0.62 | 0.72 | 0.68 |
| 10-10 01:26 | +20 | BTC | DOWN | 0.62 | 0.82 | 1.72 |
| 10-10 01:26 | +15 | BTC | DOWN | 0.62 | 0.82 | 1.72 |
| 10-10 01:26 | +10 | BTC | DOWN | 0.62 | 0.72 | 0.68 |
| 10-10 01:26 | +5 | BTC | DOWN | 0.62 | 0.72 | 0.68 |
| 10-10 01:26 | +10 | XRP | DOWN | 0.37 | 0.55 | 1.45 |
| 10-10 01:26 | +5 | XRP | DOWN | 0.40 | 0.55 | 1.15 |
| 10-10 01:24 | +10 stop | XRP | DOWN | 0.62 | 0.33 | -3.21 |
| 10-10 01:23 | +10 stop | XRP | DOWN | 0.56 | 0.41 | -1.85 |
| 10-10 01:23 | +10 | XRP | DOWN | 0.56 | 0.68 | 0.86 |
| 10-10 01:23 | +5 | XRP | DOWN | 0.56 | 0.68 | 0.86 |
| 10-10 01:23 | +10 stop | HYPE | DOWN | 0.56 | 0.90 | 3.18 |
| 10-10 01:22 | +5 | BNB | DOWN | 0.63 | 0.69 | 0.29 |
| 10-10 01:22 | +10 stop | XRP | DOWN | 0.53 | 0.63 | 0.65 |
| 10-10 01:22 | +10 | XRP | DOWN | 0.53 | 0.63 | 0.65 |
| 10-10 01:22 | +5 | XRP | DOWN | 0.53 | 0.63 | 0.65 |
| 10-10 01:22 | +10 stop | ETH | DOWN | 0.70 | 0.91 | 1.86 |
| 10-10 01:22 | +20 | ETH | DOWN | 0.70 | 0.91 | 1.86 |
| 10-10 01:22 | +15 | ETH | DOWN | 0.70 | 0.91 | 1.86 |
| 10-10 01:22 | +10 | ETH | DOWN | 0.70 | 0.91 | 1.88 |
| 10-10 01:22 | +5 | ETH | DOWN | 0.70 | 0.76 | 0.34 |
| 10-10 01:21 | +10 stop | HYPE | UP | 0.66 | 0.50 | -1.94 |
| 10-10 01:21 | +5 | BNB | DOWN | 0.59 | 0.65 | 0.27 |
| 10-10 01:21 | +10 stop | XRP | DOWN | 0.61 | 0.72 | 0.78 |
