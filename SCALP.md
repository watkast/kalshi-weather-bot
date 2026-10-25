# Range-Scalp Bot

*Updated Sun Oct 25 07:15 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 32741 | 28550 | 4191 (42) | 2 | $-9311.09 | -4.5% |
| **+10¢** | 24516 | 19664 | 4852 (60) | 2 | $-8310.30 | -5.4% |
| **+15¢** | 20527 | 15306 | 5221 (83) | 2 | $-7474.64 | -5.8% |
| **+20¢** | 18184 | 12718 | 5466 (105) | 2 | $-6622.36 | -5.8% |
| **+10¢ (15¢ stop)** | 40221 | 40161 | 60 (32) | 0 | $-15369.10 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-25 07:08 | +10 | NEAR | UP | 0.61 | 0.73 | 0.89 |
| 10-25 07:08 | +5 | NEAR | UP | 0.61 | 0.66 | 0.17 |
| 10-25 07:06 | +10 stop | NEAR | UP | 0.68 | 0.82 | 1.13 |
| 10-25 07:05 | +10 stop | ZEC | UP | 0.67 | 0.82 | 1.23 |
| 10-25 07:04 | +10 stop | HYPE | UP | 0.53 | 0.75 | 1.88 |
| 10-25 07:04 | +10 stop | SOL | UP | 0.70 | 0.86 | 1.36 |
| 10-25 07:04 | +10 stop | DOGE | UP | 0.71 | 0.83 | 0.95 |
| 10-25 07:04 | +20 | DOGE | UP | 0.71 | 0.91 | 1.81 |
| 10-25 07:04 | +15 | DOGE | UP | 0.71 | 0.86 | 1.26 |
| 10-25 07:04 | +10 | DOGE | UP | 0.71 | 0.83 | 0.95 |
| 10-25 07:04 | +5 | DOGE | UP | 0.71 | 0.78 | 0.42 |
| 10-25 07:03 | +5 | ZEC | DOWN | 0.67 | open |  |
| 10-25 07:02 | +10 stop | SOL | UP | 0.56 | 0.66 | 0.66 |
| 10-25 07:02 | +10 stop | ZEC | DOWN | 0.59 | 0.41 | -2.14 |
| 10-25 07:02 | +20 | ZEC | DOWN | 0.59 | open |  |
| 10-25 07:02 | +15 | ZEC | DOWN | 0.60 | open |  |
| 10-25 07:02 | +10 | ZEC | DOWN | 0.60 | open |  |
| 10-25 07:02 | +5 | ZEC | DOWN | 0.60 | 0.67 | 0.32 |
| 10-25 07:02 | +10 stop | ETH | UP | 0.69 | 0.81 | 0.94 |
| 10-25 07:02 | +20 | ETH | UP | 0.69 | 0.92 | 2.08 |
| 10-25 07:02 | +15 | ETH | UP | 0.69 | 0.84 | 1.25 |
| 10-25 07:02 | +10 | ETH | UP | 0.69 | 0.81 | 0.94 |
| 10-25 07:02 | +5 | ETH | UP | 0.69 | 0.75 | 0.31 |
| 10-25 07:02 | +10 stop | NEAR | DOWN | 0.67 | 0.52 | -1.84 |
| 10-25 07:01 | +10 stop | HYPE | DOWN | 0.70 | 0.49 | -2.47 |
| 10-25 07:01 | +20 | HYPE | DOWN | 0.70 | open |  |
| 10-25 07:01 | +15 | HYPE | DOWN | 0.70 | open |  |
| 10-25 07:01 | +10 | HYPE | DOWN | 0.70 | open |  |
| 10-25 07:01 | +5 | HYPE | DOWN | 0.71 | open |  |
| 10-25 07:01 | +10 stop | XRP | UP | 0.63 | 0.73 | 0.70 |
| 10-25 07:01 | +20 | XRP | UP | 0.63 | 0.85 | 1.95 |
| 10-25 07:01 | +15 | XRP | UP | 0.63 | 0.85 | 1.95 |
| 10-25 07:01 | +10 | XRP | UP | 0.63 | 0.73 | 0.70 |
| 10-25 07:01 | +5 | XRP | UP | 0.63 | 0.69 | 0.29 |
| 10-25 07:01 | +10 stop | BNB | UP | 0.58 | 0.69 | 0.77 |
| 10-25 07:01 | +20 | BNB | UP | 0.58 | 0.78 | 1.69 |
| 10-25 07:01 | +15 | BNB | UP | 0.58 | 0.74 | 1.28 |
| 10-25 07:01 | +10 | BNB | UP | 0.57 | 0.69 | 0.83 |
| 10-25 07:01 | +5 | BNB | UP | 0.57 | 0.69 | 0.83 |
| 10-25 07:00 | +10 stop | NEAR | UP | 0.62 | 0.42 | -2.35 |
