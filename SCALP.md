# Range-Scalp Bot

*Updated Thu Nov 05 23:08 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 48841 | 42562 | 6279 (74) | 6 | $-13859.08 | -4.5% |
| **+10¢** | 36457 | 29157 | 7300 (100) | 7 | $-12734.92 | -5.6% |
| **+15¢** | 30536 | 22675 | 7861 (129) | 8 | $-11612.62 | -6.1% |
| **+20¢** | 27133 | 18893 | 8240 (168) | 7 | $-10287.66 | -6.0% |
| **+10¢ (15¢ stop)** | 59527 | 59432 | 95 (57) | 2 | $-22027.34 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-05 23:07 | +10 stop | HYPE | DOWN | 0.53 | 0.35 | -2.14 |
| 11-05 23:06 | +10 stop | NEAR | UP | 0.55 | 0.25 | -3.32 |
| 11-05 23:06 | +10 stop | BNB | DOWN | 0.66 | open |  |
| 11-05 23:05 | +10 stop | BNB | DOWN | 0.60 | 0.79 | 1.61 |
| 11-05 23:04 | +10 stop | SOL | DOWN | 0.69 | 0.86 | 1.46 |
| 11-05 23:04 | +10 stop | HYPE | UP | 0.65 | 0.45 | -2.34 |
| 11-05 23:04 | +10 stop | NEAR | DOWN | 0.67 | 0.40 | -3.03 |
| 11-05 23:04 | +10 stop | BTC | DOWN | 0.70 | open |  |
| 11-05 23:04 | +10 stop | XRP | DOWN | 0.62 | 0.74 | 0.89 |
| 11-05 23:03 | +10 stop | ETH | DOWN | 0.71 | 0.87 | 1.37 |
| 11-05 23:03 | +10 stop | DOGE | DOWN | 0.66 | 0.80 | 1.12 |
| 11-05 23:03 | +5 | ETH | DOWN | 0.68 | 0.75 | 0.40 |
| 11-05 23:03 | +10 stop | BNB | UP | 0.64 | 0.49 | -1.85 |
| 11-05 23:03 | +20 | BNB | UP | 0.65 | open |  |
| 11-05 23:03 | +15 | BNB | UP | 0.65 | open |  |
| 11-05 23:03 | +10 | BNB | UP | 0.63 | open |  |
| 11-05 23:03 | +5 | BNB | UP | 0.62 | open |  |
| 11-05 23:03 | +10 stop | NEAR | UP | 0.63 | 0.43 | -2.35 |
| 11-05 23:03 | +20 | NEAR | UP | 0.62 | open |  |
| 11-05 23:03 | +15 | NEAR | UP | 0.62 | open |  |
| 11-05 23:03 | +10 stop | ZEC | DOWN | 0.55 | 0.67 | 0.89 |
| 11-05 23:03 | +20 | ZEC | DOWN | 0.55 | 0.75 | 1.68 |
| 11-05 23:03 | +15 | ZEC | DOWN | 0.57 | 0.75 | 1.48 |
| 11-05 23:03 | +10 | ZEC | DOWN | 0.57 | 0.67 | 0.66 |
| 11-05 23:03 | +5 | ZEC | DOWN | 0.57 | 0.67 | 0.66 |
| 11-05 23:03 | +10 | DOGE | UP | 0.55 | open |  |
| 11-05 23:03 | +5 | DOGE | UP | 0.52 | open |  |
| 11-05 23:02 | +10 stop | XRP | UP | 0.61 | 0.46 | -1.85 |
| 11-05 23:02 | +10 stop | ETH | UP | 0.53 | 0.36 | -2.05 |
| 11-05 23:02 | +15 | ETH | UP | 0.53 | open |  |
| 11-05 23:02 | +10 | ETH | UP | 0.53 | open |  |
| 11-05 23:02 | +5 | ETH | UP | 0.53 | 0.58 | 0.14 |
| 11-05 23:02 | +10 stop | DOGE | UP | 0.59 | 0.41 | -2.14 |
| 11-05 23:02 | +20 | DOGE | UP | 0.58 | open |  |
| 11-05 23:02 | +15 | DOGE | UP | 0.58 | open |  |
| 11-05 23:02 | +10 | DOGE | UP | 0.58 | 0.68 | 0.66 |
| 11-05 23:02 | +5 | DOGE | UP | 0.58 | 0.68 | 0.66 |
| 11-05 23:02 | +10 stop | SOL | UP | 0.61 | 0.46 | -1.85 |
| 11-05 23:02 | +20 | SOL | UP | 0.61 | open |  |
| 11-05 23:02 | +15 | SOL | UP | 0.62 | open |  |
