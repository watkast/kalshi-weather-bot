# Range-Scalp Bot

*Updated Fri Oct 16 11:22 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 19152 | 16647 | 2505 (28) | 5 | $-5743.33 | -4.8% |
| **+10¢** | 14431 | 11533 | 2898 (40) | 5 | $-5193.11 | -5.7% |
| **+15¢** | 12080 | 8965 | 3115 (59) | 7 | $-4668.27 | -6.2% |
| **+20¢** | 10714 | 7449 | 3265 (78) | 7 | $-4151.68 | -6.2% |
| **+10¢ (15¢ stop)** | 23551 | 23501 | 50 (29) | 5 | $-9090.93 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-16 11:21 | +10 stop | DOGE | DOWN | 0.62 | open |  |
| 10-16 11:21 | +10 | DOGE | DOWN | 0.62 | open |  |
| 10-16 11:21 | +5 | DOGE | DOWN | 0.60 | open |  |
| 10-16 11:21 | +10 stop | XRP | UP | 0.59 | open |  |
| 10-16 11:21 | +10 stop | ETH | DOWN | 0.66 | open |  |
| 10-16 11:21 | +20 | ETH | DOWN | 0.66 | open |  |
| 10-16 11:21 | +15 | ETH | DOWN | 0.66 | open |  |
| 10-16 11:21 | +10 | ETH | DOWN | 0.66 | open |  |
| 10-16 11:21 | +5 | ETH | DOWN | 0.66 | open |  |
| 10-16 11:20 | +10 stop | ZEC | UP | 0.68 | open |  |
| 10-16 11:20 | +15 | ZEC | UP | 0.67 | open |  |
| 10-16 11:20 | +10 | ZEC | UP | 0.66 | 0.77 | 0.80 |
| 10-16 11:20 | +10 stop | XRP | UP | 0.61 | 0.41 | -2.34 |
| 10-16 11:20 | +10 stop | HYPE | UP | 0.65 | open |  |
| 10-16 11:20 | +10 | HYPE | UP | 0.65 | open |  |
| 10-16 11:20 | +5 | HYPE | UP | 0.65 | 0.70 | 0.19 |
| 10-16 11:19 | +10 stop | BNB | UP | 0.68 | 0.51 | -2.04 |
| 10-16 11:19 | +10 stop | ETH | DOWN | 0.57 | 0.73 | 1.28 |
| 10-16 11:19 | +20 | ETH | DOWN | 0.57 | 0.77 | 1.69 |
| 10-16 11:19 | +15 | ETH | DOWN | 0.57 | 0.73 | 1.28 |
| 10-16 11:19 | +10 | ETH | DOWN | 0.56 | 0.73 | 1.38 |
| 10-16 11:19 | +5 | ETH | DOWN | 0.56 | 0.73 | 1.38 |
| 10-16 11:19 | +10 stop | HYPE | DOWN | 0.45 | 0.57 | 0.84 |
| 10-16 11:19 | +20 | HYPE | DOWN | 0.45 | open |  |
| 10-16 11:19 | +15 | HYPE | DOWN | 0.45 | open |  |
| 10-16 11:19 | +10 | HYPE | DOWN | 0.45 | 0.57 | 0.84 |
| 10-16 11:19 | +5 | HYPE | DOWN | 0.45 | 0.57 | 0.84 |
| 10-16 11:18 | +5 | ZEC | DOWN | 0.59 | open |  |
| 10-16 11:18 | +10 stop | BNB | DOWN | 0.64 | 0.42 | -2.59 |
| 10-16 11:18 | +15 | BNB | DOWN | 0.64 | open |  |
| 10-16 11:18 | +10 | BNB | DOWN | 0.64 | open |  |
| 10-16 11:18 | +5 | ZEC | DOWN | 0.53 | 0.58 | 0.14 |
| 10-16 11:18 | +10 stop | ZEC | UP | 0.53 | 0.71 | 1.47 |
| 10-16 11:18 | +15 | ZEC | UP | 0.53 | 0.71 | 1.47 |
| 10-16 11:18 | +10 | ZEC | UP | 0.53 | 0.71 | 1.47 |
| 10-16 11:18 | +5 | ZEC | UP | 0.53 | 0.59 | 0.25 |
| 10-16 11:18 | +5 | BNB | DOWN | 0.62 | open |  |
| 10-16 11:17 | +10 stop | BTC | UP | 0.53 | 0.72 | 1.57 |
| 10-16 11:17 | +10 | BTC | UP | 0.53 | 0.72 | 1.57 |
| 10-16 11:17 | +5 | BTC | UP | 0.53 | 0.61 | 0.45 |
