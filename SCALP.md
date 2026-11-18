# Range-Scalp Bot

*Updated Wed Nov 18 04:08 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 63572 | 55445 | 8127 (118) | 2 | $-17380.01 | -4.3% |
| **+10¢** | 47491 | 37978 | 9513 (159) | 3 | $-16307.22 | -5.5% |
| **+15¢** | 39821 | 29564 | 10257 (203) | 4 | $-14784.69 | -5.9% |
| **+20¢** | 35467 | 24703 | 10764 (258) | 5 | $-13053.14 | -5.9% |
| **+10¢ (15¢ stop)** | 77350 | 77192 | 158 (93) | 2 | $-28436.70 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-18 04:08 | +10 stop | BNB | DOWN | 0.57 | open |  |
| 11-18 04:08 | +20 | BNB | DOWN | 0.57 | open |  |
| 11-18 04:08 | +15 | BNB | DOWN | 0.57 | open |  |
| 11-18 04:08 | +10 | BNB | DOWN | 0.57 | open |  |
| 11-18 04:08 | +5 | BNB | DOWN | 0.57 | 0.62 | 0.15 |
| 11-18 04:08 | +10 stop | BTC | DOWN | 0.69 | open |  |
| 11-18 04:08 | +15 | BTC | DOWN | 0.69 | open |  |
| 11-18 04:08 | +10 | BTC | DOWN | 0.69 | open |  |
| 11-18 04:08 | +5 | BTC | DOWN | 0.69 | open |  |
| 11-18 04:07 | +10 stop | ZEC | DOWN | 0.57 | 0.28 | -3.23 |
| 11-18 04:06 | +10 stop | XRP | DOWN | 0.64 | 0.44 | -2.35 |
| 11-18 04:05 | +5 | BNB | DOWN | 0.69 | 0.74 | 0.21 |
| 11-18 04:05 | +10 | SOL | DOWN | 0.58 | 0.72 | 1.07 |
| 11-18 04:04 | +10 stop | SOL | DOWN | 0.60 | 0.72 | 0.88 |
| 11-18 04:04 | +10 stop | NEAR | DOWN | 0.63 | 0.84 | 1.84 |
| 11-18 04:04 | +5 | NEAR | DOWN | 0.60 | 0.66 | 0.23 |
| 11-18 04:04 | +5 | BNB | DOWN | 0.45 | 0.59 | 1.03 |
| 11-18 04:03 | +5 | SOL | DOWN | 0.64 | 0.72 | 0.48 |
| 11-18 04:03 | +10 stop | DOGE | DOWN | 0.62 | 0.74 | 0.89 |
| 11-18 04:03 | +20 | DOGE | DOWN | 0.62 | open |  |
| 11-18 04:03 | +15 | DOGE | DOWN | 0.62 | open |  |
| 11-18 04:03 | +10 | DOGE | DOWN | 0.62 | 0.74 | 0.89 |
| 11-18 04:03 | +5 | DOGE | DOWN | 0.62 | 0.74 | 0.89 |
| 11-18 04:03 | +5 | ETH | DOWN | 0.62 | 0.70 | 0.48 |
| 11-18 04:03 | +10 stop | HYPE | DOWN | 0.70 | 0.82 | 0.94 |
| 11-18 04:03 | +10 | HYPE | DOWN | 0.70 | 0.82 | 0.94 |
| 11-18 04:03 | +5 | HYPE | DOWN | 0.70 | 0.78 | 0.52 |
| 11-18 04:02 | +10 stop | XRP | UP | 0.54 | 0.37 | -2.05 |
| 11-18 04:02 | +20 | XRP | UP | 0.55 | open |  |
| 11-18 04:02 | +15 | XRP | UP | 0.55 | 0.71 | 1.27 |
| 11-18 04:02 | +10 | XRP | UP | 0.56 | 0.71 | 1.17 |
| 11-18 04:02 | +5 | XRP | UP | 0.56 | 0.71 | 1.17 |
| 11-18 04:02 | +10 stop | ZEC | UP | 0.70 | 0.55 | -1.83 |
| 11-18 04:02 | +20 | ZEC | UP | 0.70 | open |  |
| 11-18 04:02 | +15 | ZEC | UP | 0.70 | open |  |
| 11-18 04:02 | +10 | ZEC | UP | 0.70 | open |  |
| 11-18 04:02 | +5 | ZEC | UP | 0.70 | open |  |
| 11-18 04:02 | +10 stop | HYPE | DOWN | 0.59 | 0.69 | 0.68 |
| 11-18 04:02 | +20 | HYPE | DOWN | 0.60 | 0.82 | 1.95 |
| 11-18 04:02 | +15 | HYPE | DOWN | 0.60 | 0.78 | 1.53 |
