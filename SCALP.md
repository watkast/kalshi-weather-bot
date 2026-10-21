# Range-Scalp Bot

*Updated Wed Oct 21 20:02 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 27663 | 24091 | 3572 (39) | 3 | $-8040.76 | -4.6% |
| **+10¢** | 20794 | 16673 | 4121 (55) | 4 | $-7059.65 | -5.4% |
| **+15¢** | 17416 | 12980 | 4436 (78) | 4 | $-6308.14 | -5.8% |
| **+20¢** | 15419 | 10769 | 4650 (98) | 4 | $-5657.38 | -5.8% |
| **+10¢ (15¢ stop)** | 33934 | 33875 | 59 (32) | 3 | $-12616.77 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-21 20:01 | +5 | ZEC | DOWN | 0.64 | open |  |
| 10-21 20:01 | +10 stop | BTC | DOWN | 0.63 | open |  |
| 10-21 20:01 | +20 | BTC | DOWN | 0.64 | open |  |
| 10-21 20:01 | +15 | BTC | DOWN | 0.64 | open |  |
| 10-21 20:01 | +10 | BTC | DOWN | 0.64 | open |  |
| 10-21 20:01 | +5 | BTC | DOWN | 0.64 | open |  |
| 10-21 20:01 | +10 stop | ZEC | DOWN | 0.65 | open |  |
| 10-21 20:01 | +20 | ZEC | DOWN | 0.64 | open |  |
| 10-21 20:01 | +15 | ZEC | DOWN | 0.64 | open |  |
| 10-21 20:01 | +10 | ZEC | DOWN | 0.64 | open |  |
| 10-21 20:01 | +5 | ZEC | DOWN | 0.64 | 0.69 | 0.18 |
| 10-21 20:01 | +20 | ETH | DOWN | 0.71 | open |  |
| 10-21 20:01 | +15 | ETH | DOWN | 0.71 | open |  |
| 10-21 20:01 | +10 | ETH | DOWN | 0.71 | open |  |
| 10-21 20:01 | +5 | ETH | DOWN | 0.71 | 0.76 | 0.22 |
| 10-21 20:00 | +10 stop | HYPE | DOWN | 0.61 | open |  |
| 10-21 20:00 | +20 | HYPE | DOWN | 0.61 | open |  |
| 10-21 20:00 | +15 | HYPE | DOWN | 0.62 | open |  |
| 10-21 20:00 | +10 | HYPE | DOWN | 0.62 | open |  |
| 10-21 20:00 | +5 | HYPE | DOWN | 0.62 | open |  |
| 10-21 19:58 | +10 stop | HYPE | UP | 0.44 | 0.59 | 1.15 |
| 10-21 19:57 | +10 stop | BTC | UP | 0.60 | 0.78 | 1.50 |
| 10-21 19:56 | +10 stop | HYPE | DOWN | 0.54 | 0.36 | -2.15 |
| 10-21 19:56 | +10 stop | ETH | UP | 0.57 | 0.75 | 1.48 |
| 10-21 19:56 | +20 | ETH | UP | 0.57 | 0.80 | 2.00 |
| 10-21 19:56 | +15 | ETH | UP | 0.57 | 0.75 | 1.48 |
| 10-21 19:56 | +10 | ETH | UP | 0.57 | 0.75 | 1.48 |
| 10-21 19:56 | +5 | ETH | UP | 0.57 | 0.75 | 1.48 |
| 10-21 19:56 | +10 stop | BTC | DOWN | 0.68 | 0.41 | -3.03 |
| 10-21 19:55 | +10 stop | HYPE | UP | 0.64 | 0.42 | -2.59 |
| 10-21 19:55 | +20 | HYPE | UP | 0.64 | no | -6.61 |
| 10-21 19:55 | +15 | HYPE | UP | 0.64 | no | -6.61 |
| 10-21 19:55 | +10 | HYPE | UP | 0.64 | no | -6.61 |
| 10-21 19:55 | +5 | HYPE | UP | 0.64 | no | -6.61 |
| 10-21 19:55 | +5 | SOL | UP | 0.67 | 0.73 | 0.30 |
| 10-21 19:54 | +10 stop | NEAR | DOWN | 0.54 | 0.36 | -2.19 |
| 10-21 19:54 | +10 stop | SOL | UP | 0.64 | 0.91 | 2.44 |
| 10-21 19:53 | +10 stop | DOGE | UP | 0.54 | 0.75 | 1.82 |
| 10-21 19:53 | +10 stop | SOL | DOWN | 0.65 | 0.48 | -2.04 |
| 10-21 19:53 | +10 stop | ETH | UP | 0.46 | 0.57 | 0.74 |
