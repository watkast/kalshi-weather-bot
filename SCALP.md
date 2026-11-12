# Range-Scalp Bot

*Updated Thu Nov 12 12:14 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 56864 | 49568 | 7296 (101) | 2 | $-15661.25 | -4.4% |
| **+10¢** | 42500 | 33989 | 8511 (133) | 2 | $-14588.45 | -5.5% |
| **+15¢** | 35634 | 26473 | 9161 (167) | 3 | $-13204.51 | -5.9% |
| **+20¢** | 31743 | 22131 | 9612 (217) | 3 | $-11589.73 | -5.8% |
| **+10¢ (15¢ stop)** | 69335 | 69207 | 128 (78) | 0 | $-25632.33 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-12 12:11 | +10 stop | BNB | DOWN | 0.53 | 0.17 | -3.88 |
| 11-12 12:11 | +20 | BNB | DOWN | 0.53 | open |  |
| 11-12 12:11 | +15 | BNB | DOWN | 0.54 | open |  |
| 11-12 12:11 | +10 | BNB | DOWN | 0.55 | open |  |
| 11-12 12:11 | +5 | BNB | DOWN | 0.55 | open |  |
| 11-12 12:11 | +10 stop | HYPE | DOWN | 0.42 | 0.55 | 0.94 |
| 11-12 12:11 | +20 | HYPE | DOWN | 0.42 | open |  |
| 11-12 12:11 | +15 | HYPE | DOWN | 0.44 | open |  |
| 11-12 12:11 | +10 | HYPE | DOWN | 0.43 | 0.55 | 0.84 |
| 11-12 12:11 | +5 | HYPE | DOWN | 0.43 | 0.55 | 0.84 |
| 11-12 12:09 | +5 | ETH | DOWN | 0.69 | 0.75 | 0.31 |
| 11-12 12:08 | +15 | ETH | DOWN | 0.62 | 0.77 | 1.20 |
| 11-12 12:08 | +10 | ETH | DOWN | 0.62 | 0.75 | 0.99 |
| 11-12 12:08 | +5 | ETH | DOWN | 0.62 | 0.71 | 0.58 |
| 11-12 12:08 | +10 stop | NEAR | DOWN | 0.53 | 0.28 | -2.82 |
| 11-12 12:08 | +20 | NEAR | DOWN | 0.52 | open |  |
| 11-12 12:08 | +15 | NEAR | DOWN | 0.52 | open |  |
| 11-12 12:08 | +10 | NEAR | DOWN | 0.52 | open |  |
| 11-12 12:08 | +5 | NEAR | DOWN | 0.52 | open |  |
| 11-12 12:05 | +5 | ETH | DOWN | 0.70 | 0.78 | 0.52 |
| 11-12 12:05 | +10 stop | XRP | DOWN | 0.64 | 0.75 | 0.79 |
| 11-12 12:05 | +10 | XRP | DOWN | 0.67 | 0.80 | 1.02 |
| 11-12 12:05 | +5 | XRP | DOWN | 0.67 | 0.75 | 0.50 |
| 11-12 12:04 | +10 stop | ETH | DOWN | 0.70 | 0.82 | 0.94 |
| 11-12 12:04 | +10 stop | BNB | DOWN | 0.68 | 0.79 | 0.82 |
| 11-12 12:04 | +10 stop | BTC | DOWN | 0.61 | 0.80 | 1.61 |
| 11-12 12:03 | +10 stop | SOL | UP | 0.53 | 0.36 | -2.06 |
| 11-12 12:03 | +10 stop | ETH | UP | 0.61 | 0.34 | -3.03 |
| 11-12 12:03 | +10 stop | XRP | UP | 0.52 | 0.32 | -2.34 |
| 11-12 12:03 | +10 stop | BTC | UP | 0.66 | 0.40 | -2.93 |
| 11-12 12:02 | +5 | ETH | DOWN | 0.61 | 0.68 | 0.37 |
| 11-12 12:02 | +10 stop | XRP | DOWN | 0.56 | 0.41 | -1.85 |
| 11-12 12:02 | +20 | XRP | DOWN | 0.57 | 0.80 | 2.00 |
| 11-12 12:02 | +15 | XRP | DOWN | 0.59 | 0.75 | 1.29 |
| 11-12 12:02 | +10 | XRP | DOWN | 0.57 | 0.67 | 0.66 |
| 11-12 12:02 | +5 | XRP | DOWN | 0.56 | 0.67 | 0.75 |
| 11-12 12:02 | +10 stop | ZEC | UP | 0.62 | 0.27 | -3.81 |
| 11-12 12:02 | +20 | ZEC | UP | 0.63 | 0.97 | 3.22 |
| 11-12 12:02 | +15 | ZEC | UP | 0.62 | 0.97 | 3.32 |
| 11-12 12:02 | +10 | ZEC | UP | 0.62 | 0.72 | 0.68 |
