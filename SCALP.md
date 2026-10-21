# Range-Scalp Bot

*Updated Wed Oct 21 22:54 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 27851 | 24263 | 3588 (39) | 3 | $-8035.43 | -4.6% |
| **+10¢** | 20927 | 16785 | 4142 (55) | 4 | $-7065.26 | -5.4% |
| **+15¢** | 17527 | 13069 | 4458 (78) | 4 | $-6305.16 | -5.7% |
| **+20¢** | 15517 | 10845 | 4672 (98) | 7 | $-5642.70 | -5.8% |
| **+10¢ (15¢ stop)** | 34192 | 34133 | 59 (32) | 4 | $-12735.64 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-21 22:52 | +10 stop | BTC | DOWN | 0.67 | open |  |
| 10-21 22:52 | +5 | BTC | DOWN | 0.67 | open |  |
| 10-21 22:52 | +10 stop | SOL | DOWN | 0.64 | open |  |
| 10-21 22:51 | +5 | ZEC | UP | 0.71 | 0.78 | 0.42 |
| 10-21 22:51 | +10 stop | NEAR | DOWN | 0.60 | open |  |
| 10-21 22:51 | +10 stop | ZEC | UP | 0.68 | 0.78 | 0.71 |
| 10-21 22:51 | +20 | ZEC | UP | 0.68 | open |  |
| 10-21 22:51 | +15 | ZEC | UP | 0.70 | open |  |
| 10-21 22:51 | +10 | ZEC | UP | 0.71 | 0.81 | 0.74 |
| 10-21 22:51 | +10 stop | XRP | DOWN | 0.61 | 0.71 | 0.68 |
| 10-21 22:51 | +10 stop | SOL | DOWN | 0.57 | 0.71 | 1.07 |
| 10-21 22:51 | +10 stop | NEAR | UP | 0.45 | 0.56 | 0.74 |
| 10-21 22:51 | +10 stop | XRP | UP | 0.41 | 0.56 | 1.15 |
| 10-21 22:50 | +5 | ZEC | UP | 0.65 | 0.73 | 0.50 |
| 10-21 22:49 | +10 stop | HYPE | DOWN | 0.71 | open |  |
| 10-21 22:49 | +10 | HYPE | DOWN | 0.71 | open |  |
| 10-21 22:49 | +5 | HYPE | DOWN | 0.71 | 0.78 | 0.42 |
| 10-21 22:49 | +5 | ZEC | UP | 0.51 | 0.59 | 0.45 |
| 10-21 22:48 | +5 | ETH | DOWN | 0.70 | 0.76 | 0.32 |
| 10-21 22:48 | +10 stop | NEAR | DOWN | 0.63 | 0.44 | -2.25 |
| 10-21 22:48 | +5 | XRP | DOWN | 0.62 | 0.71 | 0.58 |
| 10-21 22:48 | +5 | DOGE | DOWN | 0.61 | 0.67 | 0.27 |
| 10-21 22:48 | +10 stop | SOL | DOWN | 0.59 | 0.40 | -2.24 |
| 10-21 22:47 | +10 stop | NEAR | UP | 0.59 | 0.35 | -2.71 |
| 10-21 22:47 | +20 | NEAR | UP | 0.59 | open |  |
| 10-21 22:47 | +15 | NEAR | UP | 0.59 | open |  |
| 10-21 22:47 | +10 | NEAR | UP | 0.59 | open |  |
| 10-21 22:47 | +5 | NEAR | UP | 0.59 | open |  |
| 10-21 22:47 | +10 stop | ZEC | UP | 0.52 | 0.63 | 0.73 |
| 10-21 22:47 | +20 | ZEC | UP | 0.52 | 0.73 | 1.76 |
| 10-21 22:47 | +15 | ZEC | UP | 0.52 | 0.69 | 1.34 |
| 10-21 22:47 | +10 | ZEC | UP | 0.53 | 0.63 | 0.65 |
| 10-21 22:47 | +5 | ZEC | UP | 0.53 | 0.60 | 0.35 |
| 10-21 22:46 | +10 stop | HYPE | DOWN | 0.63 | 0.74 | 0.79 |
| 10-21 22:46 | +20 | HYPE | DOWN | 0.63 | open |  |
| 10-21 22:46 | +15 | HYPE | DOWN | 0.63 | 0.78 | 1.20 |
| 10-21 22:46 | +10 | HYPE | DOWN | 0.63 | 0.74 | 0.79 |
| 10-21 22:46 | +5 | HYPE | DOWN | 0.63 | 0.74 | 0.79 |
| 10-21 22:46 | +10 stop | BNB | DOWN | 0.66 | 0.81 | 1.23 |
| 10-21 22:46 | +20 | BNB | DOWN | 0.66 | 0.89 | 2.07 |
