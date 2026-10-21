# Range-Scalp Bot

*Updated Wed Oct 21 04:28 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 26686 | 23240 | 3446 (33) | 1 | $-7797.05 | -4.6% |
| **+10¢** | 20084 | 16103 | 3981 (48) | 1 | $-6891.00 | -5.5% |
| **+15¢** | 16810 | 12529 | 4281 (72) | 1 | $-6127.82 | -5.8% |
| **+20¢** | 14881 | 10394 | 4487 (91) | 3 | $-5493.15 | -5.9% |
| **+10¢ (15¢ stop)** | 32701 | 32648 | 53 (30) | 0 | $-11991.09 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-21 04:28 | +10 stop | DOGE | UP | 0.22 | 0.69 | 4.42 |
| 10-21 04:28 | +20 | DOGE | UP | 0.22 | 0.69 | 4.42 |
| 10-21 04:28 | +15 | DOGE | UP | 0.23 | 0.69 | 4.32 |
| 10-21 04:28 | +10 | DOGE | UP | 0.39 | 0.69 | 2.68 |
| 10-21 04:28 | +5 | DOGE | UP | 0.44 | 0.69 | 2.17 |
| 10-21 04:27 | +10 stop | ZEC | DOWN | 0.43 | 0.55 | 0.84 |
| 10-21 04:26 | +10 stop | SOL | DOWN | 0.59 | 0.43 | -1.95 |
| 10-21 04:26 | +10 | SOL | DOWN | 0.59 | 0.82 | 2.02 |
| 10-21 04:26 | +5 | SOL | DOWN | 0.59 | 0.82 | 2.02 |
| 10-21 04:25 | +10 stop | SOL | DOWN | 0.52 | 0.64 | 0.85 |
| 10-21 04:25 | +10 | SOL | DOWN | 0.51 | 0.64 | 0.95 |
| 10-21 04:25 | +5 | SOL | DOWN | 0.50 | 0.64 | 1.05 |
| 10-21 04:25 | +5 | ETH | DOWN | 0.70 | 0.88 | 1.57 |
| 10-21 04:23 | +10 stop | BTC | UP | 0.56 | 0.74 | 1.48 |
| 10-21 04:23 | +10 stop | SOL | DOWN | 0.67 | 0.79 | 0.92 |
| 10-21 04:23 | +10 | SOL | DOWN | 0.67 | 0.79 | 0.92 |
| 10-21 04:23 | +5 | SOL | DOWN | 0.67 | 0.72 | 0.19 |
| 10-21 04:23 | +10 stop | ETH | DOWN | 0.65 | 0.42 | -2.64 |
| 10-21 04:23 | +10 | ETH | DOWN | 0.65 | 0.88 | 2.06 |
| 10-21 04:23 | +5 | ETH | DOWN | 0.65 | 0.71 | 0.29 |
| 10-21 04:23 | +10 stop | HYPE | DOWN | 0.65 | 0.50 | -1.88 |
| 10-21 04:22 | +10 stop | ZEC | DOWN | 0.68 | 0.82 | 1.13 |
| 10-21 04:22 | +5 | SOL | DOWN | 0.60 | 0.75 | 1.18 |
| 10-21 04:22 | +10 stop | ETH | DOWN | 0.57 | 0.67 | 0.66 |
| 10-21 04:21 | +10 stop | BNB | UP | 0.57 | 0.41 | -1.95 |
| 10-21 04:21 | +10 stop | NEAR | DOWN | 0.60 | 0.72 | 0.88 |
| 10-21 04:21 | +10 stop | SOL | DOWN | 0.61 | 0.75 | 1.09 |
| 10-21 04:21 | +15 | DOGE | UP | 0.64 | 0.82 | 1.52 |
| 10-21 04:21 | +10 | DOGE | UP | 0.64 | 0.82 | 1.52 |
| 10-21 04:21 | +5 | DOGE | UP | 0.64 | 0.82 | 1.52 |
| 10-21 04:21 | +10 | ZEC | UP | 0.65 | open |  |
| 10-21 04:21 | +5 | ZEC | UP | 0.65 | open |  |
| 10-21 04:20 | +10 | BTC | UP | 0.64 | 0.74 | 0.69 |
| 10-21 04:20 | +5 | BTC | UP | 0.64 | 0.74 | 0.69 |
| 10-21 04:20 | +15 | HYPE | UP | 0.69 | 0.88 | 1.67 |
| 10-21 04:20 | +10 | HYPE | UP | 0.69 | 0.88 | 1.67 |
| 10-21 04:20 | +10 stop | NEAR | UP | 0.63 | 0.41 | -2.54 |
| 10-21 04:20 | +10 stop | BNB | UP | 0.69 | 0.51 | -2.13 |
| 10-21 04:20 | +10 stop | SOL | UP | 0.65 | 0.44 | -2.44 |
| 10-21 04:20 | +10 stop | ETH | UP | 0.66 | 0.51 | -1.84 |
