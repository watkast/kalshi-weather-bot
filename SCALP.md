# Range-Scalp Bot

*Updated Sun Oct 11 17:25 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 12221 | 10539 | 1682 (24) | 1 | $-4102.17 | -5.3% |
| **+10¢** | 9286 | 7335 | 1951 (37) | 1 | $-3872.72 | -6.6% |
| **+15¢** | 7827 | 5755 | 2072 (54) | 1 | $-3320.25 | -6.8% |
| **+20¢** | 6975 | 4816 | 2159 (68) | 1 | $-2822.71 | -6.4% |
| **+10¢ (15¢ stop)** | 15052 | 15011 | 41 (25) | 1 | $-5931.01 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-11 17:24 | +20 | NEAR | DOWN | 0.71 | open |  |
| 10-11 17:24 | +15 | NEAR | DOWN | 0.71 | open |  |
| 10-11 17:23 | +10 stop | NEAR | DOWN | 0.67 | open |  |
| 10-11 17:18 | +10 stop | NEAR | UP | 0.66 | 0.49 | -2.04 |
| 10-11 17:18 | +10 | NEAR | UP | 0.66 | open |  |
| 10-11 17:18 | +5 | NEAR | UP | 0.66 | open |  |
| 10-11 17:17 | +5 | BNB | UP | 0.64 | 0.70 | 0.28 |
| 10-11 17:17 | +10 stop | NEAR | UP | 0.52 | 0.64 | 0.84 |
| 10-11 17:17 | +10 | NEAR | UP | 0.52 | 0.64 | 0.84 |
| 10-11 17:17 | +5 | NEAR | UP | 0.52 | 0.59 | 0.34 |
| 10-11 17:16 | +10 stop | ETH | UP | 0.66 | 0.77 | 0.81 |
| 10-11 17:16 | +20 | ETH | UP | 0.66 | 0.87 | 1.86 |
| 10-11 17:16 | +15 | ETH | UP | 0.66 | 0.83 | 1.44 |
| 10-11 17:16 | +10 | ETH | UP | 0.66 | 0.77 | 0.81 |
| 10-11 17:16 | +5 | ETH | UP | 0.66 | 0.75 | 0.60 |
| 10-11 17:16 | +10 stop | NEAR | DOWN | 0.46 | 0.56 | 0.64 |
| 10-11 17:16 | +20 | NEAR | DOWN | 0.46 | 0.66 | 1.66 |
| 10-11 17:16 | +15 | NEAR | DOWN | 0.46 | 0.66 | 1.66 |
| 10-11 17:16 | +10 | NEAR | DOWN | 0.46 | 0.56 | 0.64 |
| 10-11 17:16 | +5 | NEAR | DOWN | 0.46 | 0.56 | 0.64 |
| 10-11 17:16 | +10 stop | BNB | UP | 0.61 | 0.72 | 0.78 |
| 10-11 17:16 | +20 | BNB | UP | 0.61 | 0.81 | 1.72 |
| 10-11 17:16 | +15 | BNB | UP | 0.61 | 0.76 | 1.20 |
| 10-11 17:16 | +10 | BNB | UP | 0.61 | 0.72 | 0.78 |
| 10-11 17:16 | +5 | BNB | UP | 0.61 | 0.70 | 0.58 |
| 10-11 17:16 | +10 stop | DOGE | UP | 0.69 | 0.79 | 0.73 |
| 10-11 17:16 | +20 | DOGE | UP | 0.69 | 0.91 | 1.98 |
| 10-11 17:16 | +15 | DOGE | UP | 0.69 | 0.86 | 1.46 |
| 10-11 17:16 | +10 | DOGE | UP | 0.69 | 0.79 | 0.73 |
| 10-11 17:16 | +5 | DOGE | UP | 0.69 | 0.79 | 0.73 |
| 10-11 17:15 | +10 stop | SOL | UP | 0.66 | 0.76 | 0.75 |
| 10-11 17:15 | +20 | SOL | UP | 0.66 | 0.86 | 1.78 |
| 10-11 17:15 | +15 | SOL | UP | 0.65 | 0.80 | 1.22 |
| 10-11 17:15 | +10 | SOL | UP | 0.65 | 0.75 | 0.70 |
| 10-11 17:15 | +5 | SOL | UP | 0.65 | 0.74 | 0.60 |
| 10-11 17:15 | +10 stop | HYPE | UP | 0.70 | 0.80 | 0.73 |
| 10-11 17:15 | +20 | HYPE | UP | 0.70 | 0.92 | 1.94 |
| 10-11 17:15 | +15 | HYPE | UP | 0.70 | 0.87 | 1.43 |
| 10-11 17:15 | +10 | HYPE | UP | 0.70 | 0.85 | 1.22 |
| 10-11 17:15 | +5 | HYPE | UP | 0.70 | 0.76 | 0.32 |
