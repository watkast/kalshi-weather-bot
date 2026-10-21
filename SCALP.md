# Range-Scalp Bot

*Updated Wed Oct 21 02:27 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 26558 | 23128 | 3430 (33) | 0 | $-7765.10 | -4.6% |
| **+10¢** | 19981 | 16023 | 3958 (48) | 3 | $-6839.03 | -5.4% |
| **+15¢** | 16725 | 12467 | 4258 (72) | 2 | $-6092.78 | -5.8% |
| **+20¢** | 14805 | 10341 | 4464 (91) | 2 | $-5470.73 | -5.9% |
| **+10¢ (15¢ stop)** | 32534 | 32481 | 53 (30) | 0 | $-11913.81 | -5.8% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-21 02:25 | +10 stop | SOL | UP | 0.48 | 0.32 | -1.94 |
| 10-21 02:25 | +10 stop | ZEC | DOWN | 0.68 | 0.48 | -2.34 |
| 10-21 02:25 | +20 | ZEC | DOWN | 0.68 | open |  |
| 10-21 02:25 | +15 | ZEC | DOWN | 0.68 | open |  |
| 10-21 02:25 | +10 | ZEC | DOWN | 0.68 | open |  |
| 10-21 02:25 | +5 | ZEC | DOWN | 0.65 | 0.74 | 0.60 |
| 10-21 02:24 | +5 | HYPE | DOWN | 0.65 | 0.76 | 0.81 |
| 10-21 02:23 | +10 stop | SOL | DOWN | 0.64 | 0.45 | -2.25 |
| 10-21 02:23 | +15 | SOL | DOWN | 0.64 | 0.84 | 1.73 |
| 10-21 02:23 | +10 | SOL | DOWN | 0.64 | 0.84 | 1.73 |
| 10-21 02:23 | +5 | SOL | DOWN | 0.65 | 0.73 | 0.50 |
| 10-21 02:23 | +10 stop | HYPE | DOWN | 0.62 | 0.76 | 1.10 |
| 10-21 02:22 | +10 stop | BTC | DOWN | 0.71 | 0.83 | 0.95 |
| 10-21 02:22 | +10 stop | BNB | DOWN | 0.71 | 0.83 | 0.97 |
| 10-21 02:21 | +10 stop | ZEC | DOWN | 0.70 | 0.81 | 0.84 |
| 10-21 02:21 | +10 stop | BTC | DOWN | 0.53 | 0.65 | 0.86 |
| 10-21 02:21 | +5 | DOGE | DOWN | 0.71 | 0.77 | 0.32 |
| 10-21 02:21 | +10 stop | XRP | DOWN | 0.62 | 0.72 | 0.68 |
| 10-21 02:20 | +10 stop | SOL | UP | 0.64 | 0.49 | -1.85 |
| 10-21 02:20 | +10 stop | ETH | UP | 0.50 | 0.18 | -3.45 |
| 10-21 02:20 | +20 | ETH | UP | 0.50 | open |  |
| 10-21 02:20 | +15 | ETH | UP | 0.50 | open |  |
| 10-21 02:20 | +10 | ETH | UP | 0.50 | open |  |
| 10-21 02:20 | +5 | ETH | UP | 0.50 | 0.56 | 0.24 |
| 10-21 02:20 | +10 stop | DOGE | DOWN | 0.70 | 0.85 | 1.26 |
| 10-21 02:18 | +10 stop | DOGE | UP | 0.65 | 0.50 | -1.84 |
| 10-21 02:18 | +10 | DOGE | UP | 0.65 | open |  |
| 10-21 02:18 | +10 stop | BNB | UP | 0.67 | 0.49 | -2.14 |
| 10-21 02:18 | +10 stop | HYPE | UP | 0.61 | 0.34 | -3.03 |
| 10-21 02:18 | +10 stop | ZEC | UP | 0.70 | 0.48 | -2.53 |
| 10-21 02:18 | +10 stop | BTC | UP | 0.71 | 0.55 | -1.93 |
| 10-21 02:18 | +10 stop | XRP | UP | 0.69 | 0.53 | -1.93 |
| 10-21 02:17 | +10 stop | SOL | UP | 0.61 | 0.72 | 0.78 |
| 10-21 02:17 | +10 stop | ETH | UP | 0.59 | 0.71 | 0.88 |
| 10-21 02:17 | +20 | ETH | UP | 0.59 | 0.81 | 1.92 |
| 10-21 02:17 | +15 | ETH | UP | 0.59 | 0.76 | 1.40 |
| 10-21 02:17 | +10 | ETH | UP | 0.59 | 0.71 | 0.88 |
| 10-21 02:17 | +5 | ETH | UP | 0.59 | 0.71 | 0.88 |
| 10-21 02:17 | +10 stop | HYPE | DOWN | 0.62 | 0.43 | -2.29 |
| 10-21 02:17 | +20 | HYPE | DOWN | 0.62 | 0.83 | 1.79 |
