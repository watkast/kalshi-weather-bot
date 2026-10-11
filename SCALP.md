# Range-Scalp Bot

*Updated Sun Oct 11 17:55 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 12256 | 10570 | 1686 (25) | 4 | $-4100.33 | -5.3% |
| **+10¢** | 9309 | 7356 | 1953 (37) | 5 | $-3864.16 | -6.6% |
| **+15¢** | 7840 | 5768 | 2072 (54) | 6 | $-3297.08 | -6.7% |
| **+20¢** | 6988 | 4829 | 2159 (68) | 6 | $-2793.24 | -6.4% |
| **+10¢ (15¢ stop)** | 15097 | 15056 | 41 (25) | 2 | $-5948.98 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-11 17:55 | +10 stop | DOGE | UP | 0.43 | 0.59 | 1.25 |
| 10-11 17:54 | +10 stop | ETH | DOWN | 0.71 | 0.82 | 0.84 |
| 10-11 17:54 | +10 stop | BNB | DOWN | 0.69 | 0.81 | 0.94 |
| 10-11 17:54 | +10 | BNB | DOWN | 0.69 | 0.81 | 0.94 |
| 10-11 17:54 | +5 | BNB | DOWN | 0.69 | 0.81 | 0.94 |
| 10-11 17:54 | +10 stop | XRP | UP | 0.64 | open |  |
| 10-11 17:53 | +10 stop | ETH | DOWN | 0.63 | 0.74 | 0.79 |
| 10-11 17:53 | +10 | ETH | DOWN | 0.64 | 0.74 | 0.69 |
| 10-11 17:52 | +10 stop | DOGE | UP | 0.62 | 0.73 | 0.79 |
| 10-11 17:52 | +5 | BNB | DOWN | 0.64 | 0.77 | 0.96 |
| 10-11 17:52 | +10 stop | XRP | UP | 0.59 | 0.69 | 0.68 |
| 10-11 17:51 | +10 stop | BTC | DOWN | 0.66 | 0.77 | 0.81 |
| 10-11 17:51 | +10 | BTC | DOWN | 0.66 | 0.77 | 0.81 |
| 10-11 17:51 | +5 | BTC | DOWN | 0.66 | 0.75 | 0.60 |
| 10-11 17:51 | +10 stop | ETH | DOWN | 0.50 | 0.61 | 0.75 |
| 10-11 17:51 | +10 | ETH | DOWN | 0.50 | 0.61 | 0.75 |
| 10-11 17:51 | +5 | BNB | DOWN | 0.58 | 0.65 | 0.33 |
| 10-11 17:51 | +10 stop | ZEC | DOWN | 0.70 | open |  |
| 10-11 17:51 | +10 | ZEC | DOWN | 0.70 | open |  |
| 10-11 17:51 | +5 | ZEC | DOWN | 0.69 | 0.74 | 0.21 |
| 10-11 17:50 | +5 | ETH | DOWN | 0.66 | 0.74 | 0.50 |
| 10-11 17:49 | +5 | BTC | DOWN | 0.63 | 0.68 | 0.19 |
| 10-11 17:49 | +5 | HYPE | DOWN | 0.60 | open |  |
| 10-11 17:48 | +10 stop | DOGE | UP | 0.65 | 0.49 | -1.94 |
| 10-11 17:48 | +10 stop | XRP | UP | 0.53 | 0.65 | 0.87 |
| 10-11 17:48 | +10 stop | SOL | UP | 0.62 | 0.47 | -1.85 |
| 10-11 17:47 | +10 stop | HYPE | DOWN | 0.63 | 0.46 | -2.05 |
| 10-11 17:47 | +20 | HYPE | DOWN | 0.63 | open |  |
| 10-11 17:47 | +15 | HYPE | DOWN | 0.63 | open |  |
| 10-11 17:47 | +10 | HYPE | DOWN | 0.63 | open |  |
| 10-11 17:47 | +5 | HYPE | DOWN | 0.63 | 0.70 | 0.38 |
| 10-11 17:47 | +10 stop | NEAR | UP | 0.65 | 0.77 | 0.91 |
| 10-11 17:46 | +10 stop | DOGE | DOWN | 0.64 | 0.44 | -2.34 |
| 10-11 17:46 | +20 | DOGE | DOWN | 0.64 | open |  |
| 10-11 17:46 | +15 | DOGE | DOWN | 0.64 | open |  |
| 10-11 17:46 | +10 | DOGE | DOWN | 0.64 | 0.75 | 0.80 |
| 10-11 17:46 | +5 | DOGE | DOWN | 0.63 | 0.75 | 0.89 |
| 10-11 17:46 | +10 stop | SOL | DOWN | 0.59 | 0.40 | -2.24 |
| 10-11 17:46 | +20 | SOL | DOWN | 0.59 | open |  |
| 10-11 17:46 | +15 | SOL | DOWN | 0.59 | open |  |
