# Range-Scalp Bot

*Updated Wed Oct 28 07:58 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 37812 | 32995 | 4817 (45) | 0 | $-10632.78 | -4.5% |
| **+10¢** | 28231 | 22657 | 5574 (67) | 0 | $-9487.70 | -5.3% |
| **+15¢** | 23612 | 17627 | 5985 (91) | 0 | $-8455.34 | -5.7% |
| **+20¢** | 20939 | 14674 | 6265 (116) | 0 | $-7411.95 | -5.6% |
| **+10¢ (15¢ stop)** | 46320 | 46255 | 65 (34) | 0 | $-17628.29 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-28 07:53 | +5 | HYPE | UP | 0.65 | 0.71 | 0.29 |
| 10-28 07:52 | +10 stop | HYPE | UP | 0.59 | 0.71 | 0.88 |
| 10-28 07:52 | +10 | HYPE | UP | 0.59 | 0.71 | 0.88 |
| 10-28 07:52 | +5 | HYPE | UP | 0.59 | 0.64 | 0.16 |
| 10-28 07:48 | +10 stop | HYPE | UP | 0.67 | 0.77 | 0.71 |
| 10-28 07:48 | +20 | HYPE | UP | 0.67 | 0.90 | 2.10 |
| 10-28 07:48 | +15 | HYPE | UP | 0.67 | 0.90 | 2.10 |
| 10-28 07:48 | +10 | HYPE | UP | 0.67 | 0.77 | 0.71 |
| 10-28 07:48 | +5 | HYPE | UP | 0.67 | 0.73 | 0.30 |
| 10-28 07:47 | +10 stop | ZEC | UP | 0.68 | 0.78 | 0.71 |
| 10-28 07:47 | +20 | ZEC | UP | 0.68 | 0.90 | 1.97 |
| 10-28 07:47 | +15 | ZEC | UP | 0.68 | 0.83 | 1.24 |
| 10-28 07:47 | +10 | ZEC | UP | 0.68 | 0.78 | 0.71 |
| 10-28 07:47 | +5 | ZEC | UP | 0.68 | 0.75 | 0.40 |
| 10-28 07:42 | +10 stop | XRP | DOWN | 0.52 | 0.64 | 0.85 |
| 10-28 07:41 | +10 | ZEC | DOWN | 0.68 | 0.92 | 2.23 |
| 10-28 07:41 | +10 stop | XRP | UP | 0.61 | 0.38 | -2.64 |
| 10-28 07:41 | +5 | ZEC | DOWN | 0.69 | 0.92 | 2.14 |
| 10-28 07:41 | +5 | ZEC | DOWN | 0.51 | 0.62 | 0.75 |
| 10-28 07:40 | +10 stop | SOL | UP | 0.53 | 0.33 | -2.34 |
| 10-28 07:39 | +10 stop | BTC | UP | 0.60 | 0.35 | -2.83 |
| 10-28 07:39 | +15 | BTC | UP | 0.60 | no | -6.17 |
| 10-28 07:39 | +10 | BTC | UP | 0.60 | no | -6.17 |
| 10-28 07:39 | +10 stop | ETH | DOWN | 0.69 | 0.83 | 1.16 |
| 10-28 07:39 | +10 stop | XRP | UP | 0.58 | 0.42 | -1.95 |
| 10-28 07:39 | +10 stop | ZEC | DOWN | 0.53 | 0.64 | 0.75 |
| 10-28 07:39 | +20 | ZEC | DOWN | 0.53 | 0.92 | 3.71 |
| 10-28 07:39 | +15 | ZEC | DOWN | 0.53 | 0.68 | 1.16 |
| 10-28 07:39 | +10 | ZEC | DOWN | 0.52 | 0.62 | 0.65 |
| 10-28 07:39 | +5 | ZEC | DOWN | 0.53 | 0.58 | 0.14 |
| 10-28 07:38 | +10 stop | DOGE | DOWN | 0.45 | 0.15 | -3.31 |
| 10-28 07:38 | +5 | BTC | DOWN | 0.65 | 0.81 | 1.33 |
| 10-28 07:38 | +10 stop | SOL | DOWN | 0.56 | 0.40 | -1.95 |
| 10-28 07:38 | +10 stop | XRP | DOWN | 0.61 | 0.44 | -2.05 |
| 10-28 07:36 | +10 stop | BNB | UP | 0.69 | 0.48 | -2.43 |
| 10-28 07:36 | +15 | BNB | UP | 0.69 | no | -7.05 |
| 10-28 07:36 | +10 | BNB | UP | 0.69 | no | -7.05 |
| 10-28 07:35 | +5 | BNB | UP | 0.71 | no | -7.25 |
| 10-28 07:34 | +10 stop | XRP | UP | 0.61 | 0.74 | 0.99 |
| 10-28 07:34 | +10 stop | SOL | UP | 0.69 | 0.44 | -2.83 |
