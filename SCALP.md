# Range-Scalp Bot

*Updated Wed Oct 21 01:57 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 26523 | 23097 | 3426 (33) | 2 | $-7754.85 | -4.6% |
| **+10¢** | 19954 | 16000 | 3954 (48) | 2 | $-6836.68 | -5.4% |
| **+15¢** | 16702 | 12448 | 4254 (72) | 2 | $-6093.77 | -5.8% |
| **+20¢** | 14785 | 10324 | 4461 (91) | 2 | $-5483.52 | -5.9% |
| **+10¢ (15¢ stop)** | 32484 | 32431 | 53 (30) | 0 | $-11884.31 | -5.8% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-21 01:54 | +10 stop | NEAR | DOWN | 0.67 | 0.81 | 1.13 |
| 10-21 01:53 | +10 stop | NEAR | UP | 0.70 | 0.39 | -3.42 |
| 10-21 01:53 | +20 | NEAR | UP | 0.70 | open |  |
| 10-21 01:53 | +15 | NEAR | UP | 0.70 | open |  |
| 10-21 01:53 | +10 | NEAR | UP | 0.70 | open |  |
| 10-21 01:53 | +5 | NEAR | UP | 0.70 | open |  |
| 10-21 01:52 | +10 stop | ZEC | DOWN | 0.57 | 0.70 | 0.97 |
| 10-21 01:50 | +10 | ZEC | UP | 0.69 | open |  |
| 10-21 01:50 | +20 | ZEC | UP | 0.71 | open |  |
| 10-21 01:50 | +15 | ZEC | UP | 0.71 | open |  |
| 10-21 01:49 | +10 stop | ZEC | UP | 0.70 | 0.49 | -2.43 |
| 10-21 01:49 | +5 | ZEC | UP | 0.71 | open |  |
| 10-21 01:47 | +10 stop | ZEC | UP | 0.51 | 0.63 | 0.85 |
| 10-21 01:47 | +20 | ZEC | UP | 0.52 | 0.74 | 1.88 |
| 10-21 01:47 | +15 | ZEC | UP | 0.54 | 0.74 | 1.68 |
| 10-21 01:47 | +10 | ZEC | UP | 0.54 | 0.66 | 0.86 |
| 10-21 01:47 | +5 | ZEC | UP | 0.54 | 0.63 | 0.55 |
| 10-21 01:47 | +10 stop | BTC | UP | 0.69 | 0.83 | 1.15 |
| 10-21 01:47 | +20 | BTC | UP | 0.69 | 0.93 | 2.18 |
| 10-21 01:47 | +15 | BTC | UP | 0.69 | 0.86 | 1.46 |
| 10-21 01:47 | +10 | BTC | UP | 0.69 | 0.83 | 1.15 |
| 10-21 01:47 | +5 | BTC | UP | 0.69 | 0.76 | 0.42 |
| 10-21 01:46 | +10 stop | ETH | UP | 0.70 | 0.80 | 0.73 |
| 10-21 01:46 | +20 | ETH | UP | 0.70 | 0.93 | 2.09 |
| 10-21 01:46 | +15 | ETH | UP | 0.70 | 0.86 | 1.36 |
| 10-21 01:46 | +10 | ETH | UP | 0.70 | 0.80 | 0.73 |
| 10-21 01:46 | +5 | ETH | UP | 0.69 | 0.80 | 0.83 |
| 10-21 01:45 | +10 stop | NEAR | UP | 0.59 | 0.73 | 1.10 |
| 10-21 01:45 | +20 | NEAR | UP | 0.59 | 0.81 | 1.93 |
| 10-21 01:45 | +15 | NEAR | UP | 0.59 | 0.78 | 1.61 |
| 10-21 01:45 | +10 | NEAR | UP | 0.59 | 0.73 | 1.10 |
| 10-21 01:45 | +5 | NEAR | UP | 0.59 | 0.73 | 1.10 |
| 10-21 01:45 | +10 stop | XRP | UP | 0.70 | 0.82 | 0.94 |
| 10-21 01:45 | +20 | XRP | UP | 0.70 | 0.90 | 1.78 |
| 10-21 01:45 | +15 | XRP | UP | 0.70 | 0.88 | 1.57 |
| 10-21 01:45 | +10 | XRP | UP | 0.70 | 0.82 | 0.94 |
| 10-21 01:45 | +5 | XRP | UP | 0.70 | 0.75 | 0.21 |
| 10-21 01:42 | +5 | HYPE | DOWN | 0.60 | yes | -6.17 |
| 10-21 01:42 | +10 stop | NEAR | DOWN | 0.70 | 0.55 | -1.83 |
| 10-21 01:41 | +10 stop | NEAR | UP | 0.46 | 0.30 | -1.93 |
