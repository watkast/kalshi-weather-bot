# Range-Scalp Bot

*Updated Wed Oct 14 18:07 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 16314 | 14127 | 2187 (28) | 7 | $-5202.08 | -5.1% |
| **+10¢** | 12334 | 9800 | 2534 (40) | 7 | $-4802.77 | -6.2% |
| **+15¢** | 10367 | 7647 | 2720 (59) | 7 | $-4313.84 | -6.6% |
| **+20¢** | 9221 | 6369 | 2852 (76) | 7 | $-3828.66 | -6.6% |
| **+10¢ (15¢ stop)** | 20114 | 20064 | 50 (29) | 3 | $-7804.11 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-14 18:07 | +10 stop | ZEC | DOWN | 0.62 | open |  |
| 10-14 18:06 | +10 stop | ETH | UP | 0.68 | open |  |
| 10-14 18:05 | +5 | ZEC | DOWN | 0.69 | open |  |
| 10-14 18:04 | +10 stop | ETH | DOWN | 0.53 | 0.30 | -2.63 |
| 10-14 18:04 | +10 stop | NEAR | DOWN | 0.60 | 0.45 | -1.85 |
| 10-14 18:04 | +5 | ZEC | DOWN | 0.63 | 0.68 | 0.17 |
| 10-14 18:04 | +10 stop | XRP | UP | 0.66 | open |  |
| 10-14 18:03 | +10 stop | DOGE | DOWN | 0.61 | 0.46 | -1.85 |
| 10-14 18:03 | +5 | ZEC | DOWN | 0.62 | 0.67 | 0.17 |
| 10-14 18:03 | +10 stop | BTC | UP | 0.58 | 0.72 | 1.07 |
| 10-14 18:03 | +20 | BTC | UP | 0.58 | 0.81 | 2.01 |
| 10-14 18:03 | +15 | BTC | UP | 0.58 | 0.81 | 2.01 |
| 10-14 18:03 | +10 | BTC | UP | 0.58 | 0.72 | 1.07 |
| 10-14 18:03 | +5 | BTC | UP | 0.59 | 0.72 | 0.98 |
| 10-14 18:03 | +10 stop | BNB | UP | 0.60 | 0.72 | 0.88 |
| 10-14 18:02 | +10 stop | DOGE | DOWN | 0.71 | 0.54 | -2.03 |
| 10-14 18:02 | +10 | DOGE | DOWN | 0.71 | open |  |
| 10-14 18:02 | +5 | DOGE | DOWN | 0.71 | open |  |
| 10-14 18:02 | +5 | SOL | DOWN | 0.69 | open |  |
| 10-14 18:02 | +5 | SOL | DOWN | 0.61 | 0.67 | 0.27 |
| 10-14 18:02 | +5 | XRP | DOWN | 0.66 | open |  |
| 10-14 18:02 | +10 stop | NEAR | DOWN | 0.66 | 0.50 | -1.93 |
| 10-14 18:02 | +20 | NEAR | DOWN | 0.66 | open |  |
| 10-14 18:02 | +15 | NEAR | DOWN | 0.66 | open |  |
| 10-14 18:02 | +10 | NEAR | DOWN | 0.66 | open |  |
| 10-14 18:02 | +5 | NEAR | DOWN | 0.66 | open |  |
| 10-14 18:01 | +10 stop | BNB | DOWN | 0.65 | 0.50 | -1.84 |
| 10-14 18:01 | +20 | BNB | DOWN | 0.65 | open |  |
| 10-14 18:01 | +15 | BNB | DOWN | 0.65 | open |  |
| 10-14 18:01 | +10 | BNB | DOWN | 0.65 | open |  |
| 10-14 18:01 | +5 | BNB | DOWN | 0.65 | open |  |
| 10-14 18:01 | +10 stop | ETH | DOWN | 0.68 | 0.51 | -2.04 |
| 10-14 18:01 | +20 | ETH | DOWN | 0.68 | open |  |
| 10-14 18:01 | +15 | ETH | DOWN | 0.68 | open |  |
| 10-14 18:01 | +10 | ETH | DOWN | 0.68 | open |  |
| 10-14 18:01 | +5 | ETH | DOWN | 0.68 | open |  |
| 10-14 18:01 | +10 stop | DOGE | DOWN | 0.64 | 0.76 | 0.90 |
| 10-14 18:01 | +20 | DOGE | DOWN | 0.64 | open |  |
| 10-14 18:01 | +15 | DOGE | DOWN | 0.64 | open |  |
| 10-14 18:01 | +10 | DOGE | DOWN | 0.64 | 0.76 | 0.90 |
