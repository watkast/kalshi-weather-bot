# Range-Scalp Bot

*Updated Fri Oct 09 20:27 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 9451 | 8160 | 1291 (17) | 4 | $-3178.21 | -5.3% |
| **+10¢** | 7129 | 5615 | 1514 (29) | 4 | $-3103.35 | -6.9% |
| **+15¢** | 6006 | 4415 | 1591 (42) | 5 | $-2539.72 | -6.7% |
| **+20¢** | 5348 | 3695 | 1653 (53) | 5 | $-2117.83 | -6.3% |
| **+10¢ (15¢ stop)** | 11565 | 11533 | 32 (20) | 4 | $-4448.31 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-09 20:27 | +10 stop | ETH | DOWN | 0.70 | open |  |
| 10-09 20:27 | +5 | ETH | DOWN | 0.69 | open |  |
| 10-09 20:27 | +10 stop | NEAR | UP | 0.53 | open |  |
| 10-09 20:26 | +10 stop | NEAR | UP | 0.50 | 0.64 | 1.05 |
| 10-09 20:26 | +10 stop | XRP | DOWN | 0.69 | 0.54 | -1.83 |
| 10-09 20:26 | +10 | XRP | DOWN | 0.69 | open |  |
| 10-09 20:26 | +5 | XRP | DOWN | 0.69 | open |  |
| 10-09 20:26 | +10 stop | DOGE | UP | 0.58 | open |  |
| 10-09 20:26 | +5 | DOGE | UP | 0.58 | open |  |
| 10-09 20:26 | +10 stop | BTC | DOWN | 0.70 | open |  |
| 10-09 20:25 | +10 stop | HYPE | DOWN | 0.69 | 0.80 | 0.83 |
| 10-09 20:25 | +20 | HYPE | DOWN | 0.69 | 0.91 | 2.03 |
| 10-09 20:25 | +15 | HYPE | DOWN | 0.71 | 0.88 | 1.47 |
| 10-09 20:25 | +10 | HYPE | DOWN | 0.71 | 0.82 | 0.84 |
| 10-09 20:25 | +5 | HYPE | DOWN | 0.71 | 0.80 | 0.63 |
| 10-09 20:24 | +10 stop | ETH | UP | 0.68 | 0.52 | -1.94 |
| 10-09 20:24 | +20 | ETH | UP | 0.68 | open |  |
| 10-09 20:24 | +15 | ETH | UP | 0.68 | open |  |
| 10-09 20:24 | +10 | ETH | UP | 0.68 | open |  |
| 10-09 20:24 | +5 | ETH | UP | 0.68 | 0.76 | 0.51 |
| 10-09 20:24 | +10 stop | XRP | UP | 0.66 | 0.76 | 0.71 |
| 10-09 20:24 | +20 | XRP | UP | 0.66 | open |  |
| 10-09 20:24 | +15 | XRP | UP | 0.67 | open |  |
| 10-09 20:24 | +10 | XRP | UP | 0.67 | 0.77 | 0.71 |
| 10-09 20:24 | +5 | XRP | UP | 0.67 | 0.74 | 0.40 |
| 10-09 20:24 | +10 stop | DOGE | UP | 0.69 | 0.54 | -1.83 |
| 10-09 20:24 | +20 | DOGE | UP | 0.68 | open |  |
| 10-09 20:24 | +15 | DOGE | UP | 0.68 | open |  |
| 10-09 20:24 | +10 | DOGE | UP | 0.68 | open |  |
| 10-09 20:24 | +5 | DOGE | UP | 0.68 | 0.77 | 0.61 |
| 10-09 20:23 | +10 stop | BTC | UP | 0.63 | 0.73 | 0.69 |
| 10-09 20:20 | +10 stop | ETH | UP | 0.59 | 0.82 | 2.02 |
| 10-09 20:20 | +5 | XRP | UP | 0.69 | 0.82 | 0.99 |
| 10-09 20:20 | +10 stop | XRP | UP | 0.68 | 0.82 | 1.13 |
| 10-09 20:19 | +10 stop | HYPE | DOWN | 0.68 | 0.81 | 1.03 |
| 10-09 20:19 | +10 | HYPE | DOWN | 0.68 | 0.81 | 1.03 |
| 10-09 20:19 | +5 | HYPE | DOWN | 0.68 | 0.74 | 0.30 |
| 10-09 20:19 | +10 stop | BNB | UP | 0.66 | 0.88 | 1.97 |
| 10-09 20:18 | +10 stop | ETH | DOWN | 0.59 | 0.40 | -2.24 |
| 10-09 20:18 | +10 stop | BTC | DOWN | 0.64 | 0.47 | -2.05 |
