# Range-Scalp Bot

*Updated Sun Oct 04 14:11 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 2354 | 2033 | 321 (3) | 3 | $-765.85 | -5.1% |
| **+10¢** | 1836 | 1479 | 357 (4) | 4 | $-569.64 | -4.9% |
| **+15¢** | 1541 | 1164 | 377 (5) | 4 | $-466.10 | -4.8% |
| **+20¢** | 1365 | 968 | 397 (9) | 4 | $-395.60 | -4.6% |
| **+10¢ (15¢ stop)** | 2915 | 2914 | 1 (1) | 0 | $-1096.33 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-04 14:07 | +10 stop | SOL | DOWN | 0.67 | 0.52 | -1.84 |
| 10-04 14:07 | +5 | SOL | DOWN | 0.67 | 0.72 | 0.19 |
| 10-04 14:05 | +10 stop | SOL | UP | 0.68 | 0.31 | -4.01 |
| 10-04 14:04 | +10 stop | NEAR | DOWN | 0.69 | 0.81 | 0.94 |
| 10-04 14:03 | +10 stop | SOL | DOWN | 0.59 | 0.41 | -2.14 |
| 10-04 14:03 | +15 | SOL | DOWN | 0.59 | 0.76 | 1.40 |
| 10-04 14:03 | +10 | SOL | DOWN | 0.59 | 0.69 | 0.68 |
| 10-04 14:03 | +5 | SOL | DOWN | 0.59 | 0.68 | 0.57 |
| 10-04 14:03 | +10 stop | DOGE | DOWN | 0.63 | 0.43 | -2.35 |
| 10-04 14:02 | +5 | BNB | DOWN | 0.56 | 0.69 | 0.98 |
| 10-04 14:01 | +10 stop | BTC | DOWN | 0.56 | 0.66 | 0.66 |
| 10-04 14:01 | +20 | BTC | DOWN | 0.56 | 0.76 | 1.69 |
| 10-04 14:01 | +15 | BTC | DOWN | 0.56 | 0.76 | 1.69 |
| 10-04 14:01 | +10 | BTC | DOWN | 0.56 | 0.66 | 0.66 |
| 10-04 14:01 | +5 | BTC | DOWN | 0.56 | 0.66 | 0.66 |
| 10-04 14:01 | +10 stop | DOGE | UP | 0.65 | 0.33 | -3.52 |
| 10-04 14:01 | +20 | DOGE | UP | 0.65 | open |  |
| 10-04 14:01 | +15 | DOGE | UP | 0.65 | open |  |
| 10-04 14:01 | +10 | DOGE | UP | 0.65 | open |  |
| 10-04 14:01 | +5 | DOGE | UP | 0.65 | open |  |
| 10-04 14:01 | +10 stop | SOL | DOWN | 0.56 | 0.69 | 1.02 |
| 10-04 14:01 | +20 | SOL | DOWN | 0.56 | 0.76 | 1.74 |
| 10-04 14:01 | +15 | SOL | DOWN | 0.56 | 0.72 | 1.27 |
| 10-04 14:01 | +10 | SOL | DOWN | 0.56 | 0.69 | 0.97 |
| 10-04 14:01 | +5 | SOL | DOWN | 0.56 | 0.69 | 0.97 |
| 10-04 14:01 | +10 stop | ETH | DOWN | 0.68 | 0.80 | 0.92 |
| 10-04 14:01 | +20 | ETH | DOWN | 0.68 | 0.88 | 1.76 |
| 10-04 14:01 | +15 | ETH | DOWN | 0.68 | 0.87 | 1.66 |
| 10-04 14:01 | +10 | ETH | DOWN | 0.68 | 0.80 | 0.92 |
| 10-04 14:01 | +5 | ETH | DOWN | 0.68 | 0.76 | 0.51 |
| 10-04 14:00 | +10 stop | HYPE | UP | 0.68 | 0.49 | -2.28 |
| 10-04 14:00 | +20 | HYPE | UP | 0.68 | open |  |
| 10-04 14:00 | +15 | HYPE | UP | 0.68 | open |  |
| 10-04 14:00 | +10 | HYPE | UP | 0.68 | open |  |
| 10-04 14:00 | +5 | HYPE | UP | 0.68 | open |  |
| 10-04 14:00 | +10 stop | BNB | UP | 0.49 | 0.30 | -2.23 |
| 10-04 14:00 | +20 | BNB | UP | 0.49 | open |  |
| 10-04 14:00 | +15 | BNB | UP | 0.50 | open |  |
| 10-04 14:00 | +10 | BNB | UP | 0.51 | open |  |
| 10-04 14:00 | +5 | BNB | UP | 0.49 | 0.54 | 0.14 |
