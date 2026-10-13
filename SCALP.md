# Range-Scalp Bot

*Updated Tue Oct 13 11:10 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 14548 | 12578 | 1970 (27) | 0 | $-4720.56 | -5.1% |
| **+10¢** | 11008 | 8721 | 2287 (39) | 0 | $-4433.14 | -6.4% |
| **+15¢** | 9256 | 6810 | 2446 (57) | 0 | $-3941.21 | -6.8% |
| **+20¢** | 8238 | 5692 | 2546 (72) | 0 | $-3384.28 | -6.5% |
| **+10¢ (15¢ stop)** | 17859 | 17810 | 49 (29) | 0 | $-6953.18 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-13 11:02 | +10 stop | ETH | DOWN | 0.57 | 0.87 | 2.74 |
| 10-13 11:01 | +10 stop | NEAR | DOWN | 0.67 | 0.80 | 1.02 |
| 10-13 11:01 | +20 | NEAR | DOWN | 0.67 | 0.87 | 1.76 |
| 10-13 11:01 | +15 | NEAR | DOWN | 0.67 | 0.84 | 1.44 |
| 10-13 11:01 | +10 | NEAR | DOWN | 0.67 | 0.80 | 1.02 |
| 10-13 11:01 | +5 | NEAR | DOWN | 0.69 | 0.80 | 0.83 |
| 10-13 11:01 | +10 stop | BTC | DOWN | 0.68 | 0.86 | 1.55 |
| 10-13 11:01 | +20 | BTC | DOWN | 0.68 | 0.88 | 1.76 |
| 10-13 11:01 | +15 | BTC | DOWN | 0.68 | 0.86 | 1.55 |
| 10-13 11:01 | +10 | BTC | DOWN | 0.71 | 0.86 | 1.26 |
| 10-13 11:01 | +5 | BTC | DOWN | 0.71 | 0.76 | 0.22 |
| 10-13 11:01 | +10 | HYPE | DOWN | 0.69 | 0.81 | 0.94 |
| 10-13 11:01 | +5 | HYPE | DOWN | 0.69 | 0.75 | 0.31 |
| 10-13 11:01 | +10 stop | ETH | DOWN | 0.71 | 0.56 | -1.83 |
| 10-13 11:01 | +20 | ETH | DOWN | 0.71 | 0.93 | 1.99 |
| 10-13 11:01 | +15 | ETH | DOWN | 0.71 | 0.87 | 1.37 |
| 10-13 11:01 | +10 | ETH | DOWN | 0.71 | 0.87 | 1.37 |
| 10-13 11:01 | +5 | ETH | DOWN | 0.71 | 0.87 | 1.37 |
| 10-13 11:01 | +10 stop | HYPE | DOWN | 0.71 | 0.81 | 0.74 |
| 10-13 11:01 | +20 | HYPE | DOWN | 0.71 | 0.93 | 2.00 |
| 10-13 11:01 | +15 | HYPE | DOWN | 0.71 | 0.87 | 1.37 |
| 10-13 10:57 | +10 stop | XRP | UP | 0.60 | 0.72 | 0.88 |
| 10-13 10:56 | +10 stop | BTC | DOWN | 0.38 | 0.61 | 1.96 |
| 10-13 10:56 | +20 | BTC | DOWN | 0.38 | 0.61 | 1.96 |
| 10-13 10:56 | +15 | BTC | DOWN | 0.38 | 0.61 | 1.96 |
| 10-13 10:56 | +10 | BTC | DOWN | 0.38 | 0.61 | 1.96 |
| 10-13 10:56 | +5 | BTC | DOWN | 0.38 | 0.61 | 1.96 |
| 10-13 10:56 | +10 stop | XRP | DOWN | 0.61 | 0.41 | -2.34 |
| 10-13 10:56 | +10 stop | HYPE | DOWN | 0.71 | 0.49 | -2.53 |
| 10-13 10:55 | +10 stop | ZEC | DOWN | 0.70 | 0.49 | -2.46 |
| 10-13 10:53 | +10 stop | ZEC | UP | 0.70 | 0.45 | -2.83 |
| 10-13 10:52 | +10 stop | HYPE | UP | 0.63 | 0.35 | -3.13 |
| 10-13 10:52 | +10 stop | XRP | UP | 0.62 | 0.46 | -1.95 |
| 10-13 10:52 | +10 stop | XRP | DOWN | 0.35 | 0.54 | 1.56 |
| 10-13 10:50 | +5 | ETH | UP | 0.71 | 0.76 | 0.22 |
| 10-13 10:50 | +10 stop | XRP | DOWN | 0.54 | 0.67 | 0.96 |
| 10-13 10:49 | +10 stop | DOGE | UP | 0.69 | 0.86 | 1.46 |
| 10-13 10:49 | +15 | DOGE | UP | 0.69 | 0.86 | 1.46 |
| 10-13 10:49 | +10 | DOGE | UP | 0.69 | 0.86 | 1.46 |
| 10-13 10:49 | +5 | DOGE | UP | 0.69 | 0.77 | 0.52 |
