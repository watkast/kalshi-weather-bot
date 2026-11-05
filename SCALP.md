# Range-Scalp Bot

*Updated Thu Nov 05 22:07 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 48775 | 42511 | 6264 (74) | 3 | $-13798.70 | -4.5% |
| **+10¢** | 36403 | 29120 | 7283 (100) | 5 | $-12675.00 | -5.5% |
| **+15¢** | 30484 | 22640 | 7844 (129) | 7 | $-11567.40 | -6.0% |
| **+20¢** | 27083 | 18861 | 8222 (168) | 7 | $-10243.00 | -6.0% |
| **+10¢ (15¢ stop)** | 59432 | 59337 | 95 (57) | 0 | $-22002.63 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-05 22:06 | +10 stop | SOL | UP | 0.67 | 0.50 | -2.04 |
| 11-05 22:06 | +10 stop | DOGE | DOWN | 0.57 | 0.71 | 1.07 |
| 11-05 22:06 | +10 | DOGE | DOWN | 0.57 | 0.71 | 1.07 |
| 11-05 22:06 | +5 | DOGE | DOWN | 0.57 | 0.66 | 0.56 |
| 11-05 22:05 | +10 stop | NEAR | DOWN | 0.55 | 0.67 | 0.86 |
| 11-05 22:04 | +10 stop | SOL | UP | 0.58 | 0.73 | 1.18 |
| 11-05 22:04 | +10 stop | NEAR | UP | 0.68 | 0.52 | -1.94 |
| 11-05 22:04 | +10 stop | BTC | UP | 0.69 | 0.83 | 1.15 |
| 11-05 22:04 | +5 | BTC | UP | 0.69 | 0.83 | 1.15 |
| 11-05 22:04 | +10 stop | BNB | UP | 0.69 | 0.82 | 1.05 |
| 11-05 22:04 | +10 stop | DOGE | DOWN | 0.63 | 0.45 | -2.13 |
| 11-05 22:04 | +10 | DOGE | DOWN | 0.63 | 0.76 | 1.02 |
| 11-05 22:04 | +5 | DOGE | DOWN | 0.61 | 0.68 | 0.37 |
| 11-05 22:03 | +10 stop | XRP | UP | 0.67 | 0.81 | 1.13 |
| 11-05 22:03 | +10 stop | ETH | UP | 0.70 | 0.80 | 0.73 |
| 11-05 22:03 | +5 | XRP | UP | 0.70 | 0.81 | 0.84 |
| 11-05 22:03 | +5 | XRP | UP | 0.52 | 0.60 | 0.45 |
| 11-05 22:02 | +5 | DOGE | DOWN | 0.63 | 0.71 | 0.47 |
| 11-05 22:02 | +5 | SOL | DOWN | 0.61 | open |  |
| 11-05 22:02 | +10 stop | NEAR | DOWN | 0.55 | 0.38 | -2.05 |
| 11-05 22:02 | +20 | NEAR | DOWN | 0.55 | open |  |
| 11-05 22:02 | +15 | NEAR | DOWN | 0.55 | open |  |
| 11-05 22:02 | +10 | NEAR | DOWN | 0.55 | 0.67 | 0.86 |
| 11-05 22:02 | +5 | NEAR | DOWN | 0.55 | 0.67 | 0.86 |
| 11-05 22:02 | +5 | ETH | DOWN | 0.58 | open |  |
| 11-05 22:02 | +10 stop | BNB | DOWN | 0.59 | 0.41 | -2.14 |
| 11-05 22:02 | +20 | BNB | DOWN | 0.59 | open |  |
| 11-05 22:02 | +15 | BNB | DOWN | 0.59 | open |  |
| 11-05 22:02 | +10 | BNB | DOWN | 0.59 | open |  |
| 11-05 22:02 | +5 | BNB | DOWN | 0.59 | open |  |
| 11-05 22:02 | +5 | BTC | UP | 0.57 | 0.66 | 0.56 |
| 11-05 22:01 | +10 stop | SOL | DOWN | 0.63 | 0.46 | -2.05 |
| 11-05 22:01 | +20 | SOL | DOWN | 0.63 | open |  |
| 11-05 22:01 | +15 | SOL | DOWN | 0.62 | open |  |
| 11-05 22:01 | +10 | SOL | DOWN | 0.62 | open |  |
| 11-05 22:01 | +5 | SOL | DOWN | 0.61 | 0.67 | 0.27 |
| 11-05 22:01 | +10 stop | DOGE | DOWN | 0.63 | 0.75 | 0.89 |
| 11-05 22:01 | +20 | DOGE | DOWN | 0.63 | open |  |
| 11-05 22:01 | +15 | DOGE | DOWN | 0.63 | open |  |
| 11-05 22:01 | +10 | DOGE | DOWN | 0.63 | 0.75 | 0.89 |
