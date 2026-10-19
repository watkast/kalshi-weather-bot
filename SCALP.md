# Range-Scalp Bot

*Updated Mon Oct 19 09:51 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 23826 | 20716 | 3110 (31) | 4 | $-7109.16 | -4.7% |
| **+10¢** | 17925 | 14341 | 3584 (45) | 6 | $-6336.85 | -5.6% |
| **+15¢** | 15011 | 11152 | 3859 (67) | 7 | $-5742.64 | -6.1% |
| **+20¢** | 13289 | 9252 | 4037 (86) | 8 | $-5103.67 | -6.1% |
| **+10¢ (15¢ stop)** | 29319 | 29268 | 51 (30) | 2 | $-11077.78 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-19 09:50 | +5 | ETH | DOWN | 0.58 | 0.67 | 0.56 |
| 10-19 09:50 | +10 stop | HYPE | DOWN | 0.60 | open |  |
| 10-19 09:50 | +10 stop | SOL | DOWN | 0.67 | 0.78 | 0.81 |
| 10-19 09:50 | +10 stop | NEAR | DOWN | 0.61 | 0.72 | 0.78 |
| 10-19 09:50 | +20 | NEAR | DOWN | 0.61 | open |  |
| 10-19 09:50 | +15 | NEAR | DOWN | 0.61 | open |  |
| 10-19 09:50 | +10 | NEAR | DOWN | 0.61 | 0.72 | 0.78 |
| 10-19 09:50 | +5 | NEAR | DOWN | 0.61 | 0.72 | 0.78 |
| 10-19 09:50 | +10 stop | ZEC | UP | 0.59 | 0.43 | -1.95 |
| 10-19 09:50 | +10 | ZEC | UP | 0.59 | open |  |
| 10-19 09:50 | +5 | BTC | UP | 0.53 | 0.61 | 0.45 |
| 10-19 09:50 | +10 stop | DOGE | UP | 0.49 | open |  |
| 10-19 09:49 | +5 | ZEC | UP | 0.66 | open |  |
| 10-19 09:49 | +5 | ETH | DOWN | 0.53 | 0.62 | 0.55 |
| 10-19 09:48 | +5 | ETH | DOWN | 0.60 | 0.65 | 0.17 |
| 10-19 09:48 | +5 | ZEC | DOWN | 0.46 | 0.56 | 0.64 |
| 10-19 09:48 | +10 stop | SOL | DOWN | 0.69 | 0.52 | -2.03 |
| 10-19 09:48 | +10 | SOL | DOWN | 0.69 | open |  |
| 10-19 09:48 | +5 | SOL | DOWN | 0.69 | 0.78 | 0.62 |
| 10-19 09:47 | +10 stop | XRP | DOWN | 0.64 | 0.48 | -1.95 |
| 10-19 09:47 | +20 | XRP | DOWN | 0.64 | open |  |
| 10-19 09:47 | +15 | XRP | DOWN | 0.64 | open |  |
| 10-19 09:47 | +10 | XRP | DOWN | 0.64 | open |  |
| 10-19 09:47 | +5 | XRP | DOWN | 0.64 | open |  |
| 10-19 09:47 | +10 stop | ETH | DOWN | 0.59 | 0.72 | 0.98 |
| 10-19 09:47 | +20 | ETH | DOWN | 0.59 | open |  |
| 10-19 09:47 | +15 | ETH | DOWN | 0.59 | open |  |
| 10-19 09:47 | +10 | ETH | DOWN | 0.59 | 0.72 | 0.98 |
| 10-19 09:47 | +5 | ETH | DOWN | 0.59 | 0.64 | 0.16 |
| 10-19 09:47 | +10 stop | ZEC | UP | 0.52 | 0.63 | 0.75 |
| 10-19 09:47 | +20 | ZEC | UP | 0.52 | open |  |
| 10-19 09:47 | +15 | ZEC | UP | 0.52 | open |  |
| 10-19 09:47 | +10 | ZEC | UP | 0.52 | 0.63 | 0.75 |
| 10-19 09:47 | +5 | ZEC | UP | 0.52 | 0.58 | 0.24 |
| 10-19 09:47 | +10 stop | DOGE | DOWN | 0.62 | 0.47 | -1.85 |
| 10-19 09:47 | +20 | DOGE | DOWN | 0.62 | open |  |
| 10-19 09:47 | +15 | DOGE | DOWN | 0.62 | open |  |
| 10-19 09:47 | +10 | DOGE | DOWN | 0.62 | open |  |
| 10-19 09:47 | +5 | DOGE | DOWN | 0.62 | open |  |
| 10-19 09:46 | +10 stop | HYPE | DOWN | 0.69 | 0.49 | -2.37 |
