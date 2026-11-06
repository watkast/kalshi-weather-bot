# Range-Scalp Bot

*Updated Fri Nov 06 04:03 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 49155 | 42832 | 6323 (75) | 4 | $-13940.81 | -4.5% |
| **+10¢** | 36700 | 29350 | 7350 (101) | 5 | $-12796.12 | -5.5% |
| **+15¢** | 30737 | 22824 | 7913 (130) | 6 | $-11668.34 | -6.0% |
| **+20¢** | 27321 | 19027 | 8294 (170) | 5 | $-10323.90 | -6.0% |
| **+10¢ (15¢ stop)** | 59945 | 59850 | 95 (57) | 5 | $-22200.36 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-06 04:03 | +10 stop | BTC | DOWN | 0.71 | open |  |
| 11-06 04:03 | +15 | BTC | DOWN | 0.71 | open |  |
| 11-06 04:03 | +10 | BTC | DOWN | 0.71 | open |  |
| 11-06 04:03 | +5 | BNB | DOWN | 0.69 | open |  |
| 11-06 04:03 | +10 stop | SOL | DOWN | 0.64 | open |  |
| 11-06 04:03 | +20 | SOL | DOWN | 0.64 | open |  |
| 11-06 04:03 | +15 | SOL | DOWN | 0.64 | open |  |
| 11-06 04:03 | +10 | SOL | DOWN | 0.64 | open |  |
| 11-06 04:03 | +5 | SOL | DOWN | 0.64 | open |  |
| 11-06 04:02 | +10 stop | ZEC | DOWN | 0.68 | open |  |
| 11-06 04:02 | +10 | ZEC | DOWN | 0.69 | open |  |
| 11-06 04:02 | +5 | ZEC | DOWN | 0.69 | open |  |
| 11-06 04:02 | +5 | BTC | DOWN | 0.70 | 0.75 | 0.21 |
| 11-06 04:02 | +10 stop | DOGE | DOWN | 0.64 | open |  |
| 11-06 04:02 | +20 | DOGE | DOWN | 0.64 | open |  |
| 11-06 04:02 | +15 | DOGE | DOWN | 0.64 | open |  |
| 11-06 04:02 | +10 | DOGE | DOWN | 0.64 | open |  |
| 11-06 04:02 | +5 | DOGE | DOWN | 0.64 | 0.69 | 0.18 |
| 11-06 04:02 | +5 | ETH | DOWN | 0.67 | 0.73 | 0.30 |
| 11-06 04:02 | +10 stop | HYPE | DOWN | 0.57 | 0.67 | 0.66 |
| 11-06 04:02 | +20 | HYPE | DOWN | 0.57 | 0.83 | 2.32 |
| 11-06 04:02 | +15 | HYPE | DOWN | 0.57 | 0.83 | 2.32 |
| 11-06 04:02 | +10 | HYPE | DOWN | 0.57 | 0.67 | 0.66 |
| 11-06 04:02 | +5 | HYPE | DOWN | 0.57 | 0.67 | 0.66 |
| 11-06 04:02 | +10 stop | BNB | DOWN | 0.60 | 0.70 | 0.68 |
| 11-06 04:02 | +20 | BNB | DOWN | 0.60 | open |  |
| 11-06 04:02 | +15 | BNB | DOWN | 0.60 | open |  |
| 11-06 04:02 | +10 | BNB | DOWN | 0.60 | 0.70 | 0.68 |
| 11-06 04:02 | +5 | BNB | DOWN | 0.60 | 0.68 | 0.47 |
| 11-06 04:02 | +5 | NEAR | DOWN | 0.57 | 0.64 | 0.35 |
| 11-06 04:02 | +10 stop | BTC | DOWN | 0.54 | 0.69 | 1.17 |
| 11-06 04:02 | +20 | BTC | DOWN | 0.54 | 0.75 | 1.78 |
| 11-06 04:02 | +15 | BTC | DOWN | 0.54 | 0.69 | 1.17 |
| 11-06 04:02 | +10 | BTC | DOWN | 0.54 | 0.69 | 1.17 |
| 11-06 04:02 | +5 | BTC | DOWN | 0.54 | 0.62 | 0.45 |
| 11-06 04:02 | +10 stop | ETH | DOWN | 0.49 | 0.62 | 0.95 |
| 11-06 04:02 | +20 | ETH | DOWN | 0.49 | 0.73 | 2.08 |
| 11-06 04:02 | +15 | ETH | DOWN | 0.49 | 0.73 | 2.08 |
| 11-06 04:02 | +10 | ETH | DOWN | 0.49 | 0.62 | 0.95 |
| 11-06 04:02 | +5 | ETH | DOWN | 0.49 | 0.55 | 0.24 |
