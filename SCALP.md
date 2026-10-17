# Range-Scalp Bot

*Updated Sat Oct 17 06:00 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 20473 | 17813 | 2660 (29) | 4 | $-6018.08 | -4.7% |
| **+10¢** | 15417 | 12349 | 3068 (41) | 5 | $-5346.84 | -5.5% |
| **+15¢** | 12896 | 9597 | 3299 (60) | 5 | $-4803.73 | -5.9% |
| **+20¢** | 11433 | 7977 | 3456 (79) | 5 | $-4245.56 | -5.9% |
| **+10¢ (15¢ stop)** | 25155 | 25105 | 50 (29) | 0 | $-9493.47 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-17 05:57 | +10 stop | XRP | UP | 0.58 | 0.81 | 2.01 |
| 10-17 05:56 | +10 stop | BNB | UP | 0.68 | 0.96 | 2.62 |
| 10-17 05:56 | +10 stop | BTC | DOWN | 0.63 | 0.43 | -2.35 |
| 10-17 05:56 | +15 | BTC | DOWN | 0.64 | 0.84 | 1.73 |
| 10-17 05:56 | +10 | BTC | DOWN | 0.64 | 0.84 | 1.73 |
| 10-17 05:56 | +5 | BTC | DOWN | 0.64 | 0.84 | 1.73 |
| 10-17 05:53 | +10 stop | XRP | DOWN | 0.54 | 0.29 | -2.83 |
| 10-17 05:53 | +10 stop | NEAR | UP | 0.53 | 0.67 | 1.06 |
| 10-17 05:53 | +10 stop | SOL | UP | 0.63 | 0.76 | 1.01 |
| 10-17 05:53 | +10 | SOL | UP | 0.62 | 0.76 | 1.08 |
| 10-17 05:52 | +5 | SOL | UP | 0.62 | 0.72 | 0.68 |
| 10-17 05:52 | +10 stop | ZEC | DOWN | 0.60 | 0.70 | 0.68 |
| 10-17 05:52 | +20 | ZEC | DOWN | 0.60 | 0.95 | 3.29 |
| 10-17 05:52 | +15 | ZEC | DOWN | 0.60 | 0.75 | 1.19 |
| 10-17 05:52 | +10 | ZEC | DOWN | 0.60 | 0.70 | 0.68 |
| 10-17 05:52 | +5 | ZEC | DOWN | 0.60 | 0.70 | 0.68 |
| 10-17 05:52 | +10 stop | SOL | UP | 0.55 | 0.67 | 0.86 |
| 10-17 05:52 | +20 | SOL | UP | 0.56 | 0.76 | 1.69 |
| 10-17 05:52 | +15 | SOL | UP | 0.56 | 0.72 | 1.27 |
| 10-17 05:52 | +10 | SOL | UP | 0.55 | 0.67 | 0.86 |
| 10-17 05:52 | +5 | SOL | UP | 0.55 | 0.62 | 0.35 |
| 10-17 05:52 | +10 stop | ETH | UP | 0.60 | 0.71 | 0.78 |
| 10-17 05:52 | +10 stop | NEAR | UP | 0.56 | 0.67 | 0.76 |
| 10-17 05:51 | +10 stop | XRP | UP | 0.60 | 0.42 | -2.15 |
| 10-17 05:51 | +10 stop | BTC | DOWN | 0.59 | 0.77 | 1.50 |
| 10-17 05:51 | +15 | BTC | DOWN | 0.59 | 0.77 | 1.50 |
| 10-17 05:51 | +10 | BTC | DOWN | 0.59 | 0.77 | 1.50 |
| 10-17 05:51 | +5 | BTC | DOWN | 0.59 | 0.77 | 1.50 |
| 10-17 05:51 | +10 stop | BNB | DOWN | 0.55 | 0.35 | -2.34 |
| 10-17 05:50 | +10 stop | HYPE | UP | 0.71 | 0.82 | 0.84 |
| 10-17 05:50 | +5 | HYPE | UP | 0.71 | 0.78 | 0.42 |
| 10-17 05:48 | +5 | BNB | DOWN | 0.67 | open |  |
| 10-17 05:48 | +10 stop | ETH | DOWN | 0.63 | 0.45 | -2.15 |
| 10-17 05:48 | +10 | ETH | DOWN | 0.65 | open |  |
| 10-17 05:48 | +5 | SOL | DOWN | 0.62 | 0.70 | 0.48 |
| 10-17 05:48 | +5 | BTC | DOWN | 0.67 | 0.75 | 0.50 |
| 10-17 05:47 | +10 stop | XRP | DOWN | 0.62 | 0.42 | -2.35 |
| 10-17 05:47 | +5 | XRP | DOWN | 0.62 | open |  |
| 10-17 05:47 | +5 | ETH | DOWN | 0.68 | open |  |
| 10-17 05:47 | +10 stop | DOGE | UP | 0.61 | 0.81 | 1.71 |
