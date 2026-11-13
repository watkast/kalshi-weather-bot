# Range-Scalp Bot

*Updated Fri Nov 13 01:23 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 57584 | 50217 | 7367 (101) | 3 | $-15726.39 | -4.3% |
| **+10¢** | 43039 | 34433 | 8606 (133) | 5 | $-14688.32 | -5.4% |
| **+15¢** | 36081 | 26819 | 9262 (167) | 6 | $-13251.13 | -5.9% |
| **+20¢** | 32144 | 22426 | 9718 (217) | 8 | $-11614.30 | -5.8% |
| **+10¢ (15¢ stop)** | 70206 | 70078 | 128 (78) | 4 | $-25849.40 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-13 01:22 | +5 | ETH | UP | 0.71 | 0.78 | 0.42 |
| 11-13 01:22 | +5 | ZEC | DOWN | 0.57 | open |  |
| 11-13 01:22 | +5 | ZEC | DOWN | 0.42 | 0.56 | 1.04 |
| 11-13 01:21 | +10 stop | XRP | UP | 0.67 | open |  |
| 11-13 01:21 | +10 stop | DOGE | DOWN | 0.54 | open |  |
| 11-13 01:21 | +10 stop | ZEC | DOWN | 0.50 | open |  |
| 11-13 01:21 | +10 stop | SOL | DOWN | 0.54 | 0.39 | -1.88 |
| 11-13 01:21 | +10 stop | BTC | UP | 0.71 | open |  |
| 11-13 01:21 | +20 | BTC | UP | 0.71 | open |  |
| 11-13 01:21 | +15 | BTC | UP | 0.71 | open |  |
| 11-13 01:21 | +10 | BTC | UP | 0.71 | open |  |
| 11-13 01:21 | +5 | BTC | UP | 0.71 | 0.76 | 0.22 |
| 11-13 01:21 | +5 | ZEC | DOWN | 0.50 | 0.57 | 0.34 |
| 11-13 01:20 | +5 | NEAR | UP | 0.55 | 0.62 | 0.35 |
| 11-13 01:20 | +10 stop | XRP | UP | 0.66 | 0.51 | -1.84 |
| 11-13 01:20 | +20 | XRP | UP | 0.67 | open |  |
| 11-13 01:20 | +15 | XRP | UP | 0.67 | open |  |
| 11-13 01:20 | +10 | XRP | UP | 0.65 | open |  |
| 11-13 01:20 | +5 | XRP | UP | 0.64 | open |  |
| 11-13 01:19 | +10 stop | BNB | UP | 0.64 | 0.41 | -2.64 |
| 11-13 01:19 | +20 | BNB | UP | 0.64 | open |  |
| 11-13 01:19 | +15 | BNB | UP | 0.64 | 0.81 | 1.42 |
| 11-13 01:19 | +10 | BNB | UP | 0.64 | 0.81 | 1.42 |
| 11-13 01:19 | +5 | BNB | UP | 0.64 | 0.69 | 0.18 |
| 11-13 01:19 | +10 stop | ETH | UP | 0.67 | 0.78 | 0.81 |
| 11-13 01:19 | +20 | ETH | UP | 0.67 | open |  |
| 11-13 01:19 | +15 | ETH | UP | 0.67 | open |  |
| 11-13 01:19 | +10 | ETH | UP | 0.67 | 0.78 | 0.81 |
| 11-13 01:19 | +5 | ETH | UP | 0.67 | 0.72 | 0.19 |
| 11-13 01:19 | +10 stop | SOL | UP | 0.55 | 0.38 | -2.05 |
| 11-13 01:19 | +20 | SOL | UP | 0.55 | open |  |
| 11-13 01:19 | +15 | SOL | UP | 0.55 | open |  |
| 11-13 01:19 | +10 | SOL | UP | 0.55 | open |  |
| 11-13 01:19 | +5 | SOL | UP | 0.55 | 0.60 | 0.15 |
| 11-13 01:19 | +10 stop | NEAR | UP | 0.58 | 0.69 | 0.77 |
| 11-13 01:19 | +10 | NEAR | UP | 0.57 | 0.69 | 0.87 |
| 11-13 01:19 | +5 | NEAR | UP | 0.57 | 0.62 | 0.15 |
| 11-13 01:19 | +10 stop | ZEC | UP | 0.57 | 0.37 | -2.35 |
| 11-13 01:19 | +5 | ZEC | UP | 0.57 | 0.65 | 0.46 |
| 11-13 01:19 | +5 | DOGE | UP | 0.57 | open |  |
