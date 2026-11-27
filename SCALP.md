# Range-Scalp Bot

*Updated Fri Nov 27 05:32 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 73358 | 64015 | 9343 (165) | 2 | $-19594.02 | -4.2% |
| **+10¢** | 54675 | 43766 | 10909 (210) | 3 | $-18219.49 | -5.3% |
| **+15¢** | 45788 | 34037 | 11751 (268) | 3 | $-16326.84 | -5.7% |
| **+20¢** | 40754 | 28380 | 12374 (334) | 3 | $-14718.61 | -5.8% |
| **+10¢ (15¢ stop)** | 89365 | 89153 | 212 (129) | 2 | $-33050.63 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-27 05:31 | +10 stop | ZEC | UP | 0.69 | 0.53 | -1.93 |
| 11-27 05:31 | +20 | ZEC | UP | 0.69 | open |  |
| 11-27 05:31 | +15 | ZEC | UP | 0.69 | open |  |
| 11-27 05:31 | +10 | ZEC | UP | 0.68 | open |  |
| 11-27 05:31 | +5 | ZEC | UP | 0.68 | open |  |
| 11-27 05:31 | +10 stop | NEAR | UP | 0.63 | open |  |
| 11-27 05:31 | +20 | NEAR | UP | 0.63 | open |  |
| 11-27 05:31 | +15 | NEAR | UP | 0.63 | open |  |
| 11-27 05:31 | +10 | NEAR | UP | 0.63 | open |  |
| 11-27 05:31 | +5 | NEAR | UP | 0.63 | 0.70 | 0.38 |
| 11-27 05:31 | +10 stop | HYPE | UP | 0.58 | open |  |
| 11-27 05:31 | +20 | HYPE | UP | 0.58 | open |  |
| 11-27 05:31 | +15 | HYPE | UP | 0.58 | open |  |
| 11-27 05:31 | +10 | HYPE | UP | 0.58 | open |  |
| 11-27 05:31 | +5 | HYPE | UP | 0.58 | open |  |
| 11-27 05:29 | +20 | ZEC | DOWN | 0.60 | 0.80 | 1.71 |
| 11-27 05:28 | +10 stop | ZEC | DOWN | 0.71 | 0.56 | -1.83 |
| 11-27 05:28 | +15 | ZEC | DOWN | 0.71 | 0.98 | 2.53 |
| 11-27 05:28 | +10 | ZEC | DOWN | 0.71 | 0.98 | 2.53 |
| 11-27 05:28 | +10 stop | HYPE | DOWN | 0.53 | 0.64 | 0.75 |
| 11-27 05:27 | +10 stop | HYPE | UP | 0.71 | 0.51 | -2.33 |
| 11-27 05:26 | +10 stop | ZEC | DOWN | 0.71 | 0.49 | -2.53 |
| 11-27 05:26 | +10 stop | HYPE | DOWN | 0.67 | 0.50 | -2.04 |
| 11-27 05:26 | +10 stop | NEAR | UP | 0.63 | 0.77 | 1.10 |
| 11-27 05:26 | +5 | NEAR | UP | 0.63 | 0.71 | 0.48 |
| 11-27 05:25 | +10 stop | HYPE | UP | 0.69 | 0.42 | -3.03 |
| 11-27 05:24 | +10 stop | ZEC | UP | 0.57 | 0.39 | -2.15 |
| 11-27 05:23 | +10 stop | HYPE | UP | 0.69 | 0.50 | -2.23 |
| 11-27 05:22 | +10 stop | DOGE | UP | 0.64 | 0.74 | 0.69 |
| 11-27 05:21 | +10 stop | HYPE | UP | 0.52 | 0.63 | 0.75 |
| 11-27 05:20 | +10 stop | ZEC | UP | 0.66 | 0.41 | -2.83 |
| 11-27 05:20 | +10 stop | DOGE | UP | 0.69 | 0.54 | -1.83 |
| 11-27 05:20 | +5 | ZEC | UP | 0.66 | no | -6.74 |
| 11-27 05:20 | +5 | DOGE | UP | 0.69 | 0.83 | 1.13 |
| 11-27 05:20 | +10 stop | XRP | UP | 0.71 | 0.83 | 0.95 |
| 11-27 05:20 | +5 | XRP | UP | 0.71 | 0.76 | 0.22 |
| 11-27 05:20 | +10 stop | BTC | UP | 0.63 | 0.77 | 1.10 |
| 11-27 05:20 | +5 | DOGE | DOWN | 0.40 | 0.55 | 1.15 |
| 11-27 05:20 | +5 | ZEC | DOWN | 0.56 | 0.65 | 0.56 |
| 11-27 05:19 | +20 | DOGE | DOWN | 0.51 | yes | -5.28 |
