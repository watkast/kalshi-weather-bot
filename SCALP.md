# Range-Scalp Bot

*Updated Thu Nov 05 23:38 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 48876 | 42590 | 6286 (74) | 8 | $-13889.21 | -4.5% |
| **+10¢** | 36483 | 29175 | 7308 (100) | 9 | $-12765.43 | -5.6% |
| **+15¢** | 30558 | 22686 | 7872 (129) | 9 | $-11661.57 | -6.1% |
| **+20¢** | 27153 | 18903 | 8250 (168) | 8 | $-10330.67 | -6.1% |
| **+10¢ (15¢ stop)** | 59582 | 59487 | 95 (57) | 6 | $-22071.44 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-05 23:38 | +10 stop | ZEC | DOWN | 0.65 | open |  |
| 11-05 23:38 | +10 stop | BNB | DOWN | 0.65 | open |  |
| 11-05 23:38 | +15 | NEAR | DOWN | 0.70 | open |  |
| 11-05 23:38 | +5 | NEAR | DOWN | 0.70 | 0.76 | 0.32 |
| 11-05 23:37 | +5 | HYPE | UP | 0.59 | open |  |
| 11-05 23:37 | +10 stop | BTC | UP | 0.54 | open |  |
| 11-05 23:37 | +10 stop | ETH | UP | 0.59 | open |  |
| 11-05 23:37 | +10 stop | XRP | DOWN | 0.68 | open |  |
| 11-05 23:37 | +10 stop | HYPE | UP | 0.62 | 0.46 | -1.95 |
| 11-05 23:37 | +10 | HYPE | UP | 0.62 | open |  |
| 11-05 23:37 | +5 | HYPE | UP | 0.62 | 0.67 | 0.17 |
| 11-05 23:37 | +10 stop | SOL | UP | 0.59 | open |  |
| 11-05 23:37 | +10 stop | ZEC | UP | 0.57 | 0.37 | -2.35 |
| 11-05 23:35 | +10 stop | BNB | UP | 0.53 | 0.36 | -2.05 |
| 11-05 23:35 | +10 stop | XRP | DOWN | 0.62 | 0.44 | -2.15 |
| 11-05 23:35 | +10 stop | DOGE | UP | 0.63 | 0.42 | -2.45 |
| 11-05 23:35 | +10 stop | ETH | UP | 0.63 | 0.76 | 1.00 |
| 11-05 23:33 | +10 stop | ETH | UP | 0.67 | 0.52 | -1.84 |
| 11-05 23:33 | +10 stop | NEAR | UP | 0.50 | 0.31 | -2.23 |
| 11-05 23:33 | +10 | NEAR | UP | 0.50 | open |  |
| 11-05 23:33 | +5 | NEAR | UP | 0.50 | 0.58 | 0.44 |
| 11-05 23:33 | +10 stop | ZEC | UP | 0.66 | 0.76 | 0.71 |
| 11-05 23:33 | +10 stop | SOL | UP | 0.63 | 0.74 | 0.79 |
| 11-05 23:33 | +10 stop | BTC | UP | 0.63 | 0.76 | 1.00 |
| 11-05 23:33 | +10 stop | XRP | UP | 0.60 | 0.44 | -1.95 |
| 11-05 23:33 | +10 stop | HYPE | UP | 0.61 | 0.71 | 0.68 |
| 11-05 23:33 | +20 | HYPE | UP | 0.61 | open |  |
| 11-05 23:33 | +15 | HYPE | UP | 0.61 | open |  |
| 11-05 23:33 | +10 | HYPE | UP | 0.61 | 0.71 | 0.68 |
| 11-05 23:33 | +5 | HYPE | UP | 0.61 | 0.67 | 0.27 |
| 11-05 23:33 | +10 stop | BNB | UP | 0.64 | 0.48 | -1.95 |
| 11-05 23:33 | +20 | BNB | UP | 0.64 | open |  |
| 11-05 23:33 | +15 | BNB | UP | 0.64 | open |  |
| 11-05 23:33 | +10 | BNB | UP | 0.64 | open |  |
| 11-05 23:33 | +5 | BNB | UP | 0.64 | open |  |
| 11-05 23:32 | +10 stop | DOGE | UP | 0.63 | 0.45 | -2.15 |
| 11-05 23:32 | +10 stop | ETH | UP | 0.53 | 0.70 | 1.37 |
| 11-05 23:32 | +10 stop | SOL | UP | 0.56 | 0.67 | 0.76 |
| 11-05 23:32 | +10 stop | NEAR | DOWN | 0.44 | 0.55 | 0.74 |
| 11-05 23:32 | +20 | NEAR | DOWN | 0.44 | 0.68 | 2.06 |
