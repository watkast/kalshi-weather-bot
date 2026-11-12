# Range-Scalp Bot

*Updated Thu Nov 12 22:23 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 57383 | 50039 | 7344 (101) | 4 | $-15678.81 | -4.3% |
| **+10¢** | 42886 | 34314 | 8572 (133) | 5 | $-14603.23 | -5.4% |
| **+15¢** | 35954 | 26728 | 9226 (167) | 6 | $-13179.40 | -5.8% |
| **+20¢** | 32033 | 22353 | 9680 (217) | 7 | $-11534.37 | -5.7% |
| **+10¢ (15¢ stop)** | 69976 | 69848 | 128 (78) | 2 | $-25821.27 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-12 22:23 | +5 | SOL | DOWN | 0.65 | open |  |
| 11-12 22:23 | +10 stop | BNB | DOWN | 0.67 | open |  |
| 11-12 22:23 | +15 | BNB | DOWN | 0.67 | open |  |
| 11-12 22:23 | +10 | BNB | DOWN | 0.67 | open |  |
| 11-12 22:23 | +5 | BNB | DOWN | 0.67 | open |  |
| 11-12 22:23 | +5 | HYPE | DOWN | 0.37 | 0.59 | 1.86 |
| 11-12 22:22 | +10 stop | BTC | DOWN | 0.68 | 0.46 | -2.54 |
| 11-12 22:21 | +10 stop | ETH | DOWN | 0.67 | 0.43 | -2.74 |
| 11-12 22:21 | +10 | ETH | DOWN | 0.67 | open |  |
| 11-12 22:21 | +5 | ETH | DOWN | 0.67 | open |  |
| 11-12 22:21 | +10 stop | DOGE | DOWN | 0.65 | 0.78 | 1.01 |
| 11-12 22:21 | +10 | DOGE | DOWN | 0.65 | 0.78 | 1.01 |
| 11-12 22:21 | +5 | DOGE | DOWN | 0.65 | 0.70 | 0.19 |
| 11-12 22:20 | +10 stop | HYPE | DOWN | 0.63 | 0.28 | -3.82 |
| 11-12 22:20 | +10 | HYPE | DOWN | 0.63 | open |  |
| 11-12 22:20 | +5 | HYPE | DOWN | 0.63 | 0.70 | 0.38 |
| 11-12 22:20 | +10 stop | BNB | DOWN | 0.66 | 0.85 | 1.65 |
| 11-12 22:20 | +10 stop | BTC | DOWN | 0.65 | 0.49 | -1.94 |
| 11-12 22:20 | +15 | BTC | DOWN | 0.65 | open |  |
| 11-12 22:20 | +10 | BTC | DOWN | 0.65 | open |  |
| 11-12 22:20 | +5 | BTC | DOWN | 0.65 | open |  |
| 11-12 22:18 | +5 | ETH | DOWN | 0.60 | 0.66 | 0.27 |
| 11-12 22:18 | +10 stop | SOL | DOWN | 0.69 | open |  |
| 11-12 22:18 | +20 | SOL | DOWN | 0.69 | open |  |
| 11-12 22:18 | +15 | SOL | DOWN | 0.69 | open |  |
| 11-12 22:18 | +10 | SOL | DOWN | 0.69 | open |  |
| 11-12 22:18 | +5 | SOL | DOWN | 0.69 | 0.75 | 0.31 |
| 11-12 22:18 | +10 stop | ETH | DOWN | 0.62 | 0.78 | 1.30 |
| 11-12 22:17 | +10 | ETH | DOWN | 0.54 | 0.66 | 0.86 |
| 11-12 22:17 | +5 | ETH | DOWN | 0.54 | 0.59 | 0.15 |
| 11-12 22:17 | +10 stop | BTC | DOWN | 0.51 | 0.67 | 1.26 |
| 11-12 22:17 | +20 | BTC | DOWN | 0.51 | open |  |
| 11-12 22:17 | +15 | BTC | DOWN | 0.51 | 0.67 | 1.26 |
| 11-12 22:17 | +10 | BTC | DOWN | 0.51 | 0.67 | 1.26 |
| 11-12 22:17 | +5 | BTC | DOWN | 0.51 | 0.67 | 1.26 |
| 11-12 22:16 | +10 stop | ETH | DOWN | 0.71 | 0.55 | -1.93 |
| 11-12 22:16 | +20 | ETH | DOWN | 0.71 | open |  |
| 11-12 22:16 | +15 | ETH | DOWN | 0.71 | open |  |
| 11-12 22:16 | +10 stop | NEAR | DOWN | 0.69 | 0.85 | 1.36 |
| 11-12 22:16 | +20 | NEAR | DOWN | 0.69 | open |  |
