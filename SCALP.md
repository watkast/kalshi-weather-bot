# Range-Scalp Bot

*Updated Sat Nov 21 18:10 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 67709 | 59094 | 8615 (134) | 1 | $-18186.45 | -4.3% |
| **+10¢** | 50557 | 40493 | 10064 (175) | 2 | $-16869.50 | -5.3% |
| **+15¢** | 42385 | 31537 | 10848 (225) | 3 | $-15104.01 | -5.7% |
| **+20¢** | 37726 | 26326 | 11400 (283) | 3 | $-13424.54 | -5.7% |
| **+10¢ (15¢ stop)** | 82412 | 82241 | 171 (105) | 1 | $-30229.89 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-21 18:09 | +10 stop | DOGE | UP | 0.58 | open |  |
| 11-21 18:09 | +20 | DOGE | UP | 0.58 | open |  |
| 11-21 18:09 | +10 | DOGE | UP | 0.58 | open |  |
| 11-21 18:09 | +5 | DOGE | UP | 0.58 | open |  |
| 11-21 18:08 | +10 stop | ZEC | UP | 0.69 | 0.81 | 0.94 |
| 11-21 18:08 | +20 | ZEC | UP | 0.69 | open |  |
| 11-21 18:08 | +15 | ZEC | UP | 0.69 | open |  |
| 11-21 18:08 | +10 | ZEC | UP | 0.69 | 0.81 | 0.94 |
| 11-21 18:08 | +5 | ZEC | UP | 0.69 | 0.81 | 0.94 |
| 11-21 18:06 | +10 stop | XRP | DOWN | 0.55 | 0.65 | 0.66 |
| 11-21 18:05 | +10 stop | NEAR | UP | 0.62 | 0.81 | 1.58 |
| 11-21 18:05 | +5 | NEAR | UP | 0.64 | 0.81 | 1.42 |
| 11-21 18:04 | +10 stop | ZEC | UP | 0.58 | 0.71 | 0.97 |
| 11-21 18:03 | +15 | DOGE | UP | 0.69 | open |  |
| 11-21 18:03 | +5 | BTC | UP | 0.66 | 0.73 | 0.40 |
| 11-21 18:03 | +10 stop | DOGE | UP | 0.69 | 0.82 | 1.04 |
| 11-21 18:03 | +10 | DOGE | UP | 0.69 | 0.82 | 1.04 |
| 11-21 18:03 | +5 | NEAR | UP | 0.56 | 0.62 | 0.28 |
| 11-21 18:02 | +5 | DOGE | UP | 0.69 | 0.77 | 0.52 |
| 11-21 18:02 | +10 stop | BNB | UP | 0.64 | 0.77 | 1.00 |
| 11-21 18:02 | +20 | BNB | UP | 0.64 | 0.84 | 1.73 |
| 11-21 18:02 | +15 | BNB | UP | 0.64 | 0.81 | 1.42 |
| 11-21 18:02 | +10 | BNB | UP | 0.64 | 0.77 | 1.00 |
| 11-21 18:02 | +5 | BNB | UP | 0.64 | 0.69 | 0.18 |
| 11-21 18:01 | +10 stop | ZEC | DOWN | 0.66 | 0.50 | -1.94 |
| 11-21 18:01 | +10 stop | XRP | DOWN | 0.64 | 0.49 | -1.85 |
| 11-21 18:01 | +20 | XRP | DOWN | 0.64 | 0.85 | 1.84 |
| 11-21 18:01 | +15 | XRP | DOWN | 0.63 | 0.83 | 1.73 |
| 11-21 18:01 | +10 | XRP | DOWN | 0.63 | 0.74 | 0.79 |
| 11-21 18:01 | +5 | XRP | DOWN | 0.64 | 0.74 | 0.69 |
| 11-21 18:01 | +10 stop | ETH | UP | 0.64 | 0.77 | 1.00 |
| 11-21 18:01 | +20 | ETH | UP | 0.64 | 0.84 | 1.73 |
| 11-21 18:01 | +15 | ETH | UP | 0.64 | 0.81 | 1.42 |
| 11-21 18:01 | +10 | ETH | UP | 0.64 | 0.77 | 1.00 |
| 11-21 18:01 | +5 | ETH | UP | 0.64 | 0.71 | 0.38 |
| 11-21 18:01 | +10 stop | NEAR | DOWN | 0.52 | 0.34 | -2.10 |
| 11-21 18:01 | +20 | NEAR | DOWN | 0.52 | open |  |
| 11-21 18:01 | +15 | NEAR | DOWN | 0.52 | open |  |
| 11-21 18:01 | +10 | NEAR | DOWN | 0.52 | open |  |
| 11-21 18:01 | +5 | NEAR | DOWN | 0.52 | 0.58 | 0.24 |
