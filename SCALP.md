# Range-Scalp Bot

*Updated Thu Oct 22 17:42 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 29055 | 25310 | 3745 (39) | 0 | $-8427.05 | -4.6% |
| **+10¢** | 21802 | 17469 | 4333 (55) | 0 | $-7523.54 | -5.5% |
| **+15¢** | 18250 | 13592 | 4658 (78) | 1 | $-6718.61 | -5.9% |
| **+20¢** | 16155 | 11272 | 4883 (100) | 1 | $-6045.44 | -6.0% |
| **+10¢ (15¢ stop)** | 35646 | 35587 | 59 (32) | 0 | $-13400.06 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-22 17:40 | +10 stop | BNB | DOWN | 0.68 | 0.81 | 1.03 |
| 10-22 17:40 | +20 | BNB | DOWN | 0.68 | open |  |
| 10-22 17:40 | +15 | BNB | DOWN | 0.67 | open |  |
| 10-22 17:40 | +10 | BNB | DOWN | 0.67 | 0.81 | 1.11 |
| 10-22 17:40 | +5 | BNB | DOWN | 0.68 | 0.77 | 0.61 |
| 10-22 17:39 | +10 stop | HYPE | DOWN | 0.59 | 0.69 | 0.68 |
| 10-22 17:39 | +20 | HYPE | DOWN | 0.59 | 0.85 | 2.34 |
| 10-22 17:39 | +15 | HYPE | DOWN | 0.59 | 0.85 | 2.34 |
| 10-22 17:39 | +10 | HYPE | DOWN | 0.59 | 0.69 | 0.68 |
| 10-22 17:39 | +5 | HYPE | DOWN | 0.59 | 0.69 | 0.68 |
| 10-22 17:35 | +10 stop | SOL | DOWN | 0.63 | 0.74 | 0.79 |
| 10-22 17:35 | +10 stop | ETH | UP | 0.57 | 0.40 | -2.05 |
| 10-22 17:35 | +10 stop | NEAR | UP | 0.62 | 0.32 | -3.33 |
| 10-22 17:34 | +10 stop | HYPE | UP | 0.59 | 0.29 | -3.28 |
| 10-22 17:34 | +10 stop | SOL | DOWN | 0.70 | 0.53 | -2.03 |
| 10-22 17:34 | +10 | SOL | DOWN | 0.70 | 0.87 | 1.47 |
| 10-22 17:34 | +5 | SOL | DOWN | 0.70 | 0.77 | 0.42 |
| 10-22 17:34 | +10 stop | XRP | DOWN | 0.70 | 0.51 | -2.23 |
| 10-22 17:34 | +10 | XRP | DOWN | 0.71 | 0.82 | 0.84 |
| 10-22 17:34 | +5 | XRP | DOWN | 0.71 | 0.82 | 0.84 |
| 10-22 17:34 | +5 | ETH | DOWN | 0.71 | 0.79 | 0.53 |
| 10-22 17:34 | +10 stop | BNB | DOWN | 0.67 | 0.52 | -1.84 |
| 10-22 17:34 | +10 | BNB | DOWN | 0.67 | 0.79 | 0.92 |
| 10-22 17:34 | +5 | BNB | DOWN | 0.67 | 0.75 | 0.50 |
| 10-22 17:34 | +10 stop | ZEC | DOWN | 0.58 | 0.43 | -1.86 |
| 10-22 17:34 | +20 | ZEC | DOWN | 0.59 | 0.87 | 2.55 |
| 10-22 17:34 | +15 | ZEC | DOWN | 0.59 | 0.87 | 2.55 |
| 10-22 17:34 | +10 | ZEC | DOWN | 0.59 | 0.71 | 0.88 |
| 10-22 17:34 | +5 | ZEC | DOWN | 0.59 | 0.71 | 0.88 |
| 10-22 17:32 | +10 stop | BTC | DOWN | 0.69 | 0.79 | 0.73 |
| 10-22 17:32 | +20 | BTC | DOWN | 0.69 | 0.95 | 2.39 |
| 10-22 17:32 | +15 | BTC | DOWN | 0.69 | 0.87 | 1.57 |
| 10-22 17:32 | +10 | BTC | DOWN | 0.69 | 0.79 | 0.73 |
| 10-22 17:32 | +5 | BTC | DOWN | 0.69 | 0.79 | 0.73 |
| 10-22 17:32 | +10 stop | ETH | DOWN | 0.68 | 0.39 | -3.23 |
| 10-22 17:32 | +20 | ETH | DOWN | 0.68 | 0.89 | 1.87 |
| 10-22 17:32 | +15 | ETH | DOWN | 0.68 | 0.83 | 1.24 |
| 10-22 17:32 | +10 | ETH | DOWN | 0.68 | 0.79 | 0.82 |
| 10-22 17:32 | +5 | ETH | DOWN | 0.68 | 0.76 | 0.51 |
| 10-22 17:32 | +5 | XRP | DOWN | 0.62 | 0.69 | 0.38 |
