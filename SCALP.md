# Range-Scalp Bot

*Updated Fri Oct 09 19:57 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 9419 | 8131 | 1288 (17) | 1 | $-3175.43 | -5.3% |
| **+10¢** | 7111 | 5599 | 1512 (29) | 1 | $-3111.59 | -6.9% |
| **+15¢** | 5992 | 4402 | 1590 (42) | 0 | $-2554.56 | -6.8% |
| **+20¢** | 5335 | 3683 | 1652 (53) | 0 | $-2136.90 | -6.4% |
| **+10¢ (15¢ stop)** | 11531 | 11499 | 32 (20) | 0 | $-4431.59 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-09 19:55 | +10 stop | NEAR | UP | 0.48 | 0.31 | -2.00 |
| 10-09 19:55 | +10 | NEAR | UP | 0.48 | open |  |
| 10-09 19:55 | +5 | NEAR | UP | 0.48 | open |  |
| 10-09 19:55 | +5 | DOGE | UP | 0.41 | 0.57 | 1.25 |
| 10-09 19:54 | +10 stop | NEAR | DOWN | 0.39 | 0.53 | 1.01 |
| 10-09 19:54 | +20 | NEAR | DOWN | 0.39 | 0.68 | 2.53 |
| 10-09 19:54 | +15 | NEAR | DOWN | 0.39 | 0.68 | 2.53 |
| 10-09 19:54 | +10 | NEAR | DOWN | 0.39 | 0.53 | 1.01 |
| 10-09 19:54 | +5 | NEAR | DOWN | 0.39 | 0.53 | 1.09 |
| 10-09 19:54 | +10 stop | DOGE | DOWN | 0.50 | 0.64 | 1.05 |
| 10-09 19:54 | +20 | DOGE | DOWN | 0.50 | 0.75 | 2.18 |
| 10-09 19:54 | +15 | DOGE | DOWN | 0.50 | 0.75 | 2.18 |
| 10-09 19:54 | +10 | DOGE | DOWN | 0.50 | 0.64 | 1.05 |
| 10-09 19:54 | +5 | DOGE | DOWN | 0.50 | 0.57 | 0.34 |
| 10-09 19:48 | +5 | BTC | DOWN | 0.66 | 0.74 | 0.50 |
| 10-09 19:46 | +10 stop | NEAR | DOWN | 0.62 | 0.73 | 0.79 |
| 10-09 19:46 | +20 | NEAR | DOWN | 0.62 | 0.85 | 2.04 |
| 10-09 19:46 | +15 | NEAR | DOWN | 0.63 | 0.79 | 1.31 |
| 10-09 19:46 | +10 | NEAR | DOWN | 0.62 | 0.73 | 0.79 |
| 10-09 19:46 | +5 | NEAR | DOWN | 0.63 | 0.71 | 0.48 |
| 10-09 19:46 | +10 stop | HYPE | DOWN | 0.61 | 0.74 | 0.95 |
| 10-09 19:46 | +20 | HYPE | DOWN | 0.61 | 0.82 | 1.78 |
| 10-09 19:46 | +15 | HYPE | DOWN | 0.61 | 0.77 | 1.26 |
| 10-09 19:46 | +10 | HYPE | DOWN | 0.61 | 0.74 | 0.95 |
| 10-09 19:46 | +5 | HYPE | DOWN | 0.61 | 0.67 | 0.23 |
| 10-09 19:46 | +10 stop | SOL | DOWN | 0.64 | 0.74 | 0.69 |
| 10-09 19:46 | +20 | SOL | DOWN | 0.64 | 0.84 | 1.73 |
| 10-09 19:46 | +15 | SOL | DOWN | 0.64 | 0.81 | 1.42 |
| 10-09 19:46 | +10 | SOL | DOWN | 0.64 | 0.74 | 0.69 |
| 10-09 19:46 | +5 | SOL | DOWN | 0.64 | 0.73 | 0.59 |
| 10-09 19:46 | +10 stop | ETH | DOWN | 0.68 | 0.83 | 1.25 |
| 10-09 19:46 | +20 | ETH | DOWN | 0.67 | 0.87 | 1.76 |
| 10-09 19:46 | +15 | ETH | DOWN | 0.68 | 0.83 | 1.25 |
| 10-09 19:46 | +10 | ETH | DOWN | 0.67 | 0.83 | 1.34 |
| 10-09 19:46 | +5 | ETH | DOWN | 0.67 | 0.83 | 1.34 |
| 10-09 19:46 | +10 stop | BTC | DOWN | 0.61 | 0.74 | 0.99 |
| 10-09 19:46 | +20 | BTC | DOWN | 0.61 | 0.83 | 1.93 |
| 10-09 19:46 | +15 | BTC | DOWN | 0.61 | 0.83 | 1.93 |
| 10-09 19:46 | +10 | BTC | DOWN | 0.61 | 0.74 | 0.99 |
| 10-09 19:46 | +5 | BTC | DOWN | 0.61 | 0.66 | 0.17 |
