# Range-Scalp Bot

*Updated Tue Oct 13 21:00 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 14954 | 12929 | 2025 (27) | 0 | $-4884.91 | -5.2% |
| **+10¢** | 11317 | 8970 | 2347 (39) | 0 | $-4552.53 | -6.4% |
| **+15¢** | 9509 | 6999 | 2510 (58) | 0 | $-4038.70 | -6.8% |
| **+20¢** | 8460 | 5842 | 2618 (74) | 0 | $-3504.19 | -6.6% |
| **+10¢ (15¢ stop)** | 18354 | 18304 | 50 (29) | 0 | $-7128.35 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-13 20:58 | +10 stop | DOGE | DOWN | 0.59 | 0.39 | -2.34 |
| 10-13 20:57 | +10 stop | DOGE | UP | 0.39 | 0.62 | 1.96 |
| 10-13 20:57 | +10 stop | NEAR | UP | 0.57 | 0.25 | -3.52 |
| 10-13 20:57 | +10 | NEAR | UP | 0.57 | no | -5.88 |
| 10-13 20:57 | +5 | NEAR | UP | 0.57 | no | -5.88 |
| 10-13 20:57 | +10 stop | HYPE | DOWN | 0.62 | 0.27 | -3.81 |
| 10-13 20:56 | +10 stop | SOL | UP | 0.70 | 0.85 | 1.26 |
| 10-13 20:56 | +10 | SOL | UP | 0.70 | 0.85 | 1.26 |
| 10-13 20:56 | +5 | SOL | UP | 0.70 | 0.76 | 0.32 |
| 10-13 20:54 | +10 stop | HYPE | DOWN | 0.62 | 0.72 | 0.68 |
| 10-13 20:53 | +10 stop | BNB | UP | 0.62 | 0.75 | 0.99 |
| 10-13 20:53 | +10 | BNB | UP | 0.62 | 0.75 | 0.99 |
| 10-13 20:53 | +5 | BNB | UP | 0.64 | 0.75 | 0.80 |
| 10-13 20:53 | +10 stop | DOGE | DOWN | 0.71 | 0.56 | -1.83 |
| 10-13 20:53 | +5 | NEAR | UP | 0.65 | 0.72 | 0.39 |
| 10-13 20:51 | +10 stop | HYPE | DOWN | 0.57 | 0.68 | 0.76 |
| 10-13 20:50 | +10 stop | DOGE | DOWN | 0.58 | 0.68 | 0.66 |
| 10-13 20:50 | +10 stop | XRP | DOWN | 0.65 | 0.49 | -1.96 |
| 10-13 20:50 | +5 | NEAR | UP | 0.68 | 0.73 | 0.20 |
| 10-13 20:50 | +5 | BNB | UP | 0.67 | 0.78 | 0.81 |
| 10-13 20:50 | +10 stop | ZEC | DOWN | 0.68 | 0.80 | 0.92 |
| 10-13 20:49 | +10 | SOL | UP | 0.68 | 0.80 | 0.92 |
| 10-13 20:49 | +5 | SOL | UP | 0.68 | 0.80 | 0.92 |
| 10-13 20:49 | +10 stop | NEAR | UP | 0.67 | 0.51 | -1.94 |
| 10-13 20:49 | +20 | NEAR | UP | 0.65 | no | -6.66 |
| 10-13 20:49 | +15 | NEAR | UP | 0.65 | no | -6.66 |
| 10-13 20:49 | +10 | NEAR | UP | 0.65 | 0.76 | 0.81 |
| 10-13 20:49 | +5 | NEAR | UP | 0.66 | 0.72 | 0.29 |
| 10-13 20:49 | +10 stop | SOL | UP | 0.66 | 0.42 | -2.74 |
| 10-13 20:49 | +20 | SOL | UP | 0.66 | 0.91 | 2.28 |
| 10-13 20:49 | +15 | SOL | UP | 0.66 | 0.85 | 1.65 |
| 10-13 20:48 | +10 stop | ZEC | DOWN | 0.57 | 0.69 | 0.87 |
| 10-13 20:47 | +5 | BNB | UP | 0.68 | 0.75 | 0.36 |
| 10-13 20:47 | +10 stop | ETH | UP | 0.69 | 0.88 | 1.67 |
| 10-13 20:47 | +20 | ETH | UP | 0.69 | 0.91 | 1.98 |
| 10-13 20:47 | +15 | ETH | UP | 0.69 | 0.88 | 1.67 |
| 10-13 20:47 | +10 | ETH | UP | 0.69 | 0.88 | 1.67 |
| 10-13 20:47 | +5 | ETH | UP | 0.69 | 0.76 | 0.42 |
| 10-13 20:47 | +10 stop | ZEC | UP | 0.66 | 0.45 | -2.44 |
| 10-13 20:47 | +20 | ZEC | UP | 0.66 | no | -6.76 |
