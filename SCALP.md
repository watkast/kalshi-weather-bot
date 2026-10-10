# Range-Scalp Bot

*Updated Sat Oct 10 20:30 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 10844 | 9343 | 1501 (22) | 0 | $-3737.19 | -5.5% |
| **+10¢** | 8213 | 6467 | 1746 (36) | 0 | $-3553.61 | -6.9% |
| **+15¢** | 6929 | 5081 | 1848 (52) | 0 | $-3012.93 | -6.9% |
| **+20¢** | 6162 | 4237 | 1925 (66) | 0 | $-2569.77 | -6.6% |
| **+10¢ (15¢ stop)** | 13353 | 13312 | 41 (25) | 0 | $-5342.58 | -6.4% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-10 20:26 | +10 stop | BTC | UP | 0.67 | 0.82 | 1.23 |
| 10-10 20:25 | +10 stop | BNB | DOWN | 0.63 | 0.39 | -2.74 |
| 10-10 20:25 | +10 stop | BTC | UP | 0.55 | 0.66 | 0.76 |
| 10-10 20:25 | +10 stop | HYPE | DOWN | 0.70 | 0.92 | 2.00 |
| 10-10 20:25 | +20 | HYPE | DOWN | 0.70 | 0.92 | 2.00 |
| 10-10 20:25 | +15 | HYPE | DOWN | 0.70 | 0.92 | 2.00 |
| 10-10 20:25 | +10 | HYPE | DOWN | 0.70 | 0.92 | 2.00 |
| 10-10 20:25 | +5 | HYPE | DOWN | 0.70 | 0.92 | 2.00 |
| 10-10 20:24 | +10 stop | BNB | DOWN | 0.51 | 0.26 | -2.82 |
| 10-10 20:24 | +10 stop | XRP | DOWN | 0.61 | 0.38 | -2.64 |
| 10-10 20:24 | +10 | XRP | DOWN | 0.61 | yes | -6.27 |
| 10-10 20:24 | +5 | XRP | DOWN | 0.61 | yes | -6.27 |
| 10-10 20:21 | +5 | BTC | DOWN | 0.66 | 0.93 | 2.48 |
| 10-10 20:20 | +10 stop | BTC | DOWN | 0.65 | 0.41 | -2.73 |
| 10-10 20:20 | +10 stop | BNB | DOWN | 0.65 | 0.48 | -2.04 |
| 10-10 20:19 | +10 stop | NEAR | UP | 0.55 | 0.69 | 1.07 |
| 10-10 20:19 | +10 stop | BTC | UP | 0.55 | 0.39 | -1.95 |
| 10-10 20:19 | +10 stop | DOGE | DOWN | 0.53 | 0.75 | 1.89 |
| 10-10 20:19 | +20 | DOGE | DOWN | 0.53 | 0.75 | 1.89 |
| 10-10 20:19 | +15 | DOGE | DOWN | 0.53 | 0.75 | 1.89 |
| 10-10 20:19 | +10 | DOGE | DOWN | 0.53 | 0.75 | 1.89 |
| 10-10 20:19 | +5 | DOGE | DOWN | 0.53 | 0.62 | 0.56 |
| 10-10 20:18 | +10 stop | BNB | DOWN | 0.71 | 0.49 | -2.51 |
| 10-10 20:18 | +20 | BNB | DOWN | 0.67 | yes | -6.86 |
| 10-10 20:18 | +15 | BNB | DOWN | 0.68 | yes | -6.96 |
| 10-10 20:18 | +10 | BNB | DOWN | 0.68 | yes | -6.96 |
| 10-10 20:18 | +5 | BNB | DOWN | 0.68 | yes | -6.96 |
| 10-10 20:18 | +10 stop | NEAR | DOWN | 0.65 | 0.50 | -1.84 |
| 10-10 20:18 | +5 | BTC | DOWN | 0.58 | 0.65 | 0.36 |
| 10-10 20:17 | +10 stop | XRP | DOWN | 0.64 | 0.42 | -2.55 |
| 10-10 20:17 | +20 | XRP | DOWN | 0.64 | yes | -6.57 |
| 10-10 20:17 | +15 | XRP | DOWN | 0.64 | yes | -6.57 |
| 10-10 20:17 | +10 | XRP | DOWN | 0.64 | 0.77 | 1.00 |
| 10-10 20:17 | +5 | XRP | DOWN | 0.64 | 0.73 | 0.59 |
| 10-10 20:16 | +10 stop | BTC | DOWN | 0.70 | 0.51 | -2.23 |
| 10-10 20:16 | +20 | BTC | DOWN | 0.70 | 0.93 | 2.09 |
| 10-10 20:16 | +15 | BTC | DOWN | 0.70 | 0.93 | 2.09 |
| 10-10 20:16 | +10 | BTC | DOWN | 0.70 | 0.93 | 2.09 |
| 10-10 20:16 | +5 | BTC | DOWN | 0.70 | 0.76 | 0.32 |
| 10-10 20:16 | +10 stop | HYPE | DOWN | 0.69 | 0.80 | 0.78 |
