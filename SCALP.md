# Range-Scalp Bot

*Updated Tue Oct 06 23:45 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 5646 | 4890 | 756 (9) | 0 | $-1749.55 | -4.9% |
| **+10¢** | 4307 | 3415 | 892 (15) | 0 | $-1692.17 | -6.2% |
| **+15¢** | 3614 | 2669 | 945 (19) | 0 | $-1482.02 | -6.5% |
| **+20¢** | 3228 | 2246 | 982 (26) | 0 | $-1205.82 | -6.0% |
| **+10¢ (15¢ stop)** | 6879 | 6864 | 15 (9) | 0 | $-2476.57 | -5.7% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-06 23:42 | +10 stop | SOL | UP | 0.51 | 0.87 | 3.34 |
| 10-06 23:41 | +10 stop | BNB | DOWN | 0.53 | 0.34 | -2.23 |
| 10-06 23:41 | +15 | BNB | DOWN | 0.53 | yes | -5.47 |
| 10-06 23:41 | +10 | BNB | DOWN | 0.53 | yes | -5.47 |
| 10-06 23:41 | +5 | BNB | DOWN | 0.53 | yes | -5.47 |
| 10-06 23:41 | +15 | SOL | DOWN | 0.52 | yes | -5.41 |
| 10-06 23:40 | +10 stop | SOL | DOWN | 0.65 | 0.49 | -1.94 |
| 10-06 23:40 | +10 | SOL | DOWN | 0.65 | yes | -6.66 |
| 10-06 23:40 | +5 | SOL | DOWN | 0.65 | yes | -6.66 |
| 10-06 23:39 | +10 stop | BTC | UP | 0.63 | 0.81 | 1.52 |
| 10-06 23:39 | +10 stop | SOL | DOWN | 0.50 | 0.61 | 0.75 |
| 10-06 23:39 | +20 | SOL | DOWN | 0.50 | yes | -5.18 |
| 10-06 23:39 | +15 | SOL | DOWN | 0.50 | 0.66 | 1.26 |
| 10-06 23:39 | +10 | SOL | DOWN | 0.50 | 0.61 | 0.75 |
| 10-06 23:39 | +5 | SOL | DOWN | 0.50 | 0.61 | 0.75 |
| 10-06 23:39 | +10 stop | BNB | DOWN | 0.58 | 0.75 | 1.38 |
| 10-06 23:39 | +15 | BNB | DOWN | 0.58 | 0.75 | 1.38 |
| 10-06 23:39 | +10 | BNB | DOWN | 0.58 | 0.75 | 1.38 |
| 10-06 23:39 | +5 | BNB | DOWN | 0.58 | 0.75 | 1.38 |
| 10-06 23:39 | +5 | ETH | DOWN | 0.50 | 0.59 | 0.55 |
| 10-06 23:38 | +10 stop | ETH | DOWN | 0.61 | 0.44 | -2.05 |
| 10-06 23:38 | +20 | ETH | DOWN | 0.61 | yes | -6.27 |
| 10-06 23:38 | +15 | ETH | DOWN | 0.61 | yes | -6.27 |
| 10-06 23:38 | +10 | ETH | DOWN | 0.61 | yes | -6.27 |
| 10-06 23:38 | +5 | ETH | DOWN | 0.61 | 0.68 | 0.37 |
| 10-06 23:38 | +10 stop | BTC | DOWN | 0.56 | 0.40 | -1.95 |
| 10-06 23:38 | +20 | BTC | DOWN | 0.56 | yes | -5.78 |
| 10-06 23:38 | +15 | BTC | DOWN | 0.56 | yes | -5.78 |
| 10-06 23:38 | +10 | BTC | DOWN | 0.56 | yes | -5.78 |
| 10-06 23:38 | +5 | BTC | DOWN | 0.56 | yes | -5.78 |
| 10-06 23:36 | +10 stop | DOGE | UP | 0.71 | 0.87 | 1.37 |
| 10-06 23:36 | +5 | DOGE | UP | 0.71 | 0.87 | 1.37 |
| 10-06 23:35 | +5 | DOGE | DOWN | 0.50 | 0.57 | 0.34 |
| 10-06 23:35 | +5 | DOGE | DOWN | 0.58 | 0.64 | 0.25 |
| 10-06 23:34 | +10 stop | DOGE | DOWN | 0.65 | 0.50 | -1.84 |
| 10-06 23:33 | +10 stop | ZEC | DOWN | 0.66 | 0.79 | 1.00 |
| 10-06 23:33 | +10 stop | DOGE | DOWN | 0.59 | 0.44 | -1.85 |
| 10-06 23:33 | +5 | DOGE | DOWN | 0.57 | 0.63 | 0.23 |
| 10-06 23:32 | +5 | HYPE | DOWN | 0.71 | 0.79 | 0.53 |
| 10-06 23:32 | +10 | BNB | DOWN | 0.68 | 0.84 | 1.34 |
