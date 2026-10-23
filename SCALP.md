# Range-Scalp Bot

*Updated Fri Oct 23 19:42 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 30849 | 26885 | 3964 (39) | 2 | $-8914.37 | -4.6% |
| **+10¢** | 23080 | 18498 | 4582 (57) | 2 | $-7925.09 | -5.5% |
| **+15¢** | 19309 | 14376 | 4933 (80) | 1 | $-7164.20 | -5.9% |
| **+20¢** | 17103 | 11939 | 5164 (103) | 2 | $-6389.14 | -5.9% |
| **+10¢ (15¢ stop)** | 37851 | 37792 | 59 (32) | 0 | $-14424.97 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-23 19:38 | +10 stop | XRP | UP | 0.45 | 0.22 | -2.60 |
| 10-23 19:38 | +5 | XRP | UP | 0.44 | 0.52 | 0.44 |
| 10-23 19:38 | +10 stop | HYPE | DOWN | 0.64 | 0.78 | 1.06 |
| 10-23 19:38 | +10 | HYPE | DOWN | 0.64 | 0.78 | 1.06 |
| 10-23 19:38 | +5 | HYPE | DOWN | 0.65 | 0.78 | 1.01 |
| 10-23 19:38 | +10 stop | BNB | UP | 0.67 | 0.50 | -2.04 |
| 10-23 19:37 | +10 stop | BTC | DOWN | 0.62 | 0.74 | 0.89 |
| 10-23 19:37 | +20 | BTC | DOWN | 0.62 | open |  |
| 10-23 19:37 | +15 | BTC | DOWN | 0.62 | 0.78 | 1.30 |
| 10-23 19:37 | +10 | BTC | DOWN | 0.62 | 0.74 | 0.89 |
| 10-23 19:37 | +5 | BTC | DOWN | 0.62 | 0.74 | 0.89 |
| 10-23 19:37 | +10 stop | ETH | UP | 0.61 | 0.34 | -3.03 |
| 10-23 19:37 | +10 | ETH | UP | 0.61 | open |  |
| 10-23 19:37 | +5 | ETH | UP | 0.61 | open |  |
| 10-23 19:37 | +10 stop | XRP | DOWN | 0.49 | 0.61 | 0.85 |
| 10-23 19:37 | +15 | XRP | DOWN | 0.51 | 0.77 | 2.29 |
| 10-23 19:37 | +10 | XRP | DOWN | 0.53 | 0.77 | 2.09 |
| 10-23 19:37 | +5 | XRP | DOWN | 0.53 | 0.61 | 0.45 |
| 10-23 19:37 | +10 stop | ETH | DOWN | 0.44 | 0.55 | 0.74 |
| 10-23 19:37 | +20 | ETH | DOWN | 0.44 | 0.65 | 1.76 |
| 10-23 19:37 | +15 | ETH | DOWN | 0.44 | 0.65 | 1.76 |
| 10-23 19:37 | +10 | ETH | DOWN | 0.44 | 0.55 | 0.74 |
| 10-23 19:37 | +5 | ETH | DOWN | 0.44 | 0.55 | 0.74 |
| 10-23 19:37 | +10 stop | HYPE | DOWN | 0.55 | 0.65 | 0.66 |
| 10-23 19:37 | +20 | HYPE | DOWN | 0.55 | 0.78 | 1.99 |
| 10-23 19:37 | +15 | HYPE | DOWN | 0.55 | 0.78 | 1.99 |
| 10-23 19:37 | +10 | HYPE | DOWN | 0.55 | 0.65 | 0.66 |
| 10-23 19:37 | +5 | HYPE | DOWN | 0.55 | 0.65 | 0.66 |
| 10-23 19:37 | +5 | BNB | DOWN | 0.52 | open |  |
| 10-23 19:37 | +10 stop | ZEC | UP | 0.66 | 0.78 | 0.91 |
| 10-23 19:36 | +10 stop | ZEC | DOWN | 0.43 | 0.58 | 1.14 |
| 10-23 19:34 | +5 | BNB | DOWN | 0.66 | 0.71 | 0.19 |
| 10-23 19:34 | +10 stop | ZEC | DOWN | 0.61 | 0.43 | -2.15 |
| 10-23 19:33 | +5 | BNB | DOWN | 0.67 | 0.73 | 0.30 |
| 10-23 19:33 | +5 | ETH | DOWN | 0.70 | 0.76 | 0.32 |
| 10-23 19:32 | +10 stop | ZEC | UP | 0.61 | 0.41 | -2.34 |
| 10-23 19:32 | +20 | ZEC | UP | 0.60 | 0.87 | 2.45 |
| 10-23 19:32 | +15 | ZEC | UP | 0.59 | 0.78 | 1.60 |
| 10-23 19:32 | +10 | ZEC | UP | 0.59 | 0.78 | 1.60 |
| 10-23 19:32 | +5 | ZEC | UP | 0.59 | 0.64 | 0.16 |
