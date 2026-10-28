# Range-Scalp Bot

*Updated Wed Oct 28 06:57 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 37755 | 32947 | 4808 (45) | 1 | $-10603.83 | -4.5% |
| **+10¢** | 28189 | 22627 | 5562 (67) | 1 | $-9443.29 | -5.3% |
| **+15¢** | 23577 | 17604 | 5973 (91) | 1 | $-8416.25 | -5.7% |
| **+20¢** | 20907 | 14654 | 6253 (116) | 1 | $-7385.62 | -5.6% |
| **+10¢ (15¢ stop)** | 46242 | 46177 | 65 (34) | 0 | $-17579.37 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-28 06:55 | +10 stop | DOGE | DOWN | 0.64 | 0.79 | 1.21 |
| 10-28 06:55 | +20 | DOGE | DOWN | 0.64 | 0.85 | 1.84 |
| 10-28 06:55 | +15 | DOGE | DOWN | 0.64 | 0.79 | 1.21 |
| 10-28 06:55 | +10 | DOGE | DOWN | 0.64 | 0.79 | 1.21 |
| 10-28 06:55 | +5 | DOGE | DOWN | 0.64 | 0.70 | 0.28 |
| 10-28 06:55 | +10 stop | XRP | DOWN | 0.60 | 0.75 | 1.19 |
| 10-28 06:49 | +5 | DOGE | DOWN | 0.64 | 0.69 | 0.18 |
| 10-28 06:49 | +10 stop | XRP | DOWN | 0.59 | 0.72 | 0.98 |
| 10-28 06:48 | +10 stop | DOGE | DOWN | 0.65 | 0.77 | 0.91 |
| 10-28 06:48 | +10 | DOGE | DOWN | 0.65 | 0.77 | 0.91 |
| 10-28 06:48 | +5 | DOGE | DOWN | 0.64 | 0.69 | 0.18 |
| 10-28 06:47 | +10 stop | XRP | DOWN | 0.64 | 0.49 | -1.85 |
| 10-28 06:47 | +5 | ETH | DOWN | 0.69 | 0.75 | 0.31 |
| 10-28 06:47 | +10 stop | NEAR | DOWN | 0.61 | 0.71 | 0.68 |
| 10-28 06:47 | +20 | NEAR | DOWN | 0.61 | 0.81 | 1.72 |
| 10-28 06:47 | +15 | NEAR | DOWN | 0.61 | 0.76 | 1.20 |
| 10-28 06:47 | +10 | NEAR | DOWN | 0.61 | 0.71 | 0.68 |
| 10-28 06:47 | +5 | NEAR | DOWN | 0.61 | 0.70 | 0.58 |
| 10-28 06:47 | +5 | SOL | DOWN | 0.68 | 0.75 | 0.40 |
| 10-28 06:46 | +10 stop | XRP | UP | 0.58 | 0.39 | -2.25 |
| 10-28 06:46 | +20 | XRP | UP | 0.58 | open |  |
| 10-28 06:46 | +15 | XRP | UP | 0.58 | open |  |
| 10-28 06:46 | +10 | XRP | UP | 0.58 | open |  |
| 10-28 06:46 | +5 | XRP | UP | 0.58 | open |  |
| 10-28 06:46 | +10 stop | ZEC | DOWN | 0.61 | 0.71 | 0.68 |
| 10-28 06:46 | +20 | ZEC | DOWN | 0.61 | 0.82 | 1.82 |
| 10-28 06:46 | +15 | ZEC | DOWN | 0.61 | 0.76 | 1.20 |
| 10-28 06:46 | +10 | ZEC | DOWN | 0.61 | 0.71 | 0.68 |
| 10-28 06:46 | +5 | ZEC | DOWN | 0.61 | 0.71 | 0.68 |
| 10-28 06:46 | +10 stop | SOL | DOWN | 0.59 | 0.71 | 0.88 |
| 10-28 06:46 | +20 | SOL | DOWN | 0.59 | 0.79 | 1.71 |
| 10-28 06:46 | +15 | SOL | DOWN | 0.59 | 0.75 | 1.29 |
| 10-28 06:46 | +10 | SOL | DOWN | 0.59 | 0.71 | 0.88 |
| 10-28 06:46 | +5 | SOL | DOWN | 0.58 | 0.63 | 0.15 |
| 10-28 06:46 | +10 stop | ETH | DOWN | 0.61 | 0.75 | 1.09 |
| 10-28 06:46 | +20 | ETH | DOWN | 0.61 | 0.86 | 2.24 |
| 10-28 06:46 | +15 | ETH | DOWN | 0.61 | 0.79 | 1.51 |
| 10-28 06:46 | +10 | ETH | DOWN | 0.61 | 0.75 | 1.09 |
| 10-28 06:46 | +5 | ETH | DOWN | 0.61 | 0.66 | 0.17 |
| 10-28 06:46 | +10 stop | HYPE | DOWN | 0.67 | 0.84 | 1.40 |
