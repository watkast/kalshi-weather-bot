# Range-Scalp Bot

*Updated Fri Nov 13 02:03 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 57634 | 50263 | 7371 (101) | 1 | $-15727.96 | -4.3% |
| **+10¢** | 43074 | 34467 | 8607 (133) | 1 | $-14658.54 | -5.4% |
| **+15¢** | 36111 | 26847 | 9264 (167) | 3 | $-13219.08 | -5.8% |
| **+20¢** | 32173 | 22453 | 9720 (217) | 3 | $-11570.13 | -5.7% |
| **+10¢ (15¢ stop)** | 70270 | 70142 | 128 (78) | 1 | $-25885.38 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-13 02:02 | +5 | ETH | DOWN | 0.67 | 0.74 | 0.40 |
| 11-13 02:02 | +10 stop | NEAR | DOWN | 0.68 | 0.80 | 0.92 |
| 11-13 02:02 | +20 | NEAR | DOWN | 0.68 | open |  |
| 11-13 02:02 | +15 | NEAR | DOWN | 0.68 | open |  |
| 11-13 02:02 | +10 | NEAR | DOWN | 0.68 | 0.80 | 0.92 |
| 11-13 02:02 | +5 | NEAR | DOWN | 0.68 | 0.76 | 0.51 |
| 11-13 02:01 | +10 stop | ETH | DOWN | 0.61 | 0.74 | 0.99 |
| 11-13 02:01 | +20 | ETH | DOWN | 0.60 | open |  |
| 11-13 02:01 | +15 | ETH | DOWN | 0.61 | open |  |
| 11-13 02:01 | +10 | ETH | DOWN | 0.61 | 0.74 | 0.99 |
| 11-13 02:01 | +5 | ETH | DOWN | 0.61 | 0.67 | 0.27 |
| 11-13 02:01 | +10 stop | BTC | DOWN | 0.67 | open |  |
| 11-13 02:01 | +20 | BTC | DOWN | 0.66 | open |  |
| 11-13 02:01 | +15 | BTC | DOWN | 0.66 | open |  |
| 11-13 02:01 | +10 | BTC | DOWN | 0.66 | open |  |
| 11-13 02:01 | +5 | BTC | DOWN | 0.67 | open |  |
| 11-13 02:01 | +10 stop | DOGE | DOWN | 0.65 | 0.76 | 0.81 |
| 11-13 02:01 | +20 | DOGE | DOWN | 0.65 | 0.85 | 1.75 |
| 11-13 02:01 | +15 | DOGE | DOWN | 0.64 | 0.82 | 1.52 |
| 11-13 02:01 | +10 | DOGE | DOWN | 0.64 | 0.76 | 0.90 |
| 11-13 02:01 | +5 | DOGE | DOWN | 0.64 | 0.71 | 0.38 |
| 11-13 02:00 | +10 stop | ZEC | DOWN | 0.65 | 0.76 | 0.81 |
| 11-13 02:00 | +20 | ZEC | DOWN | 0.65 | 0.86 | 1.85 |
| 11-13 02:00 | +15 | ZEC | DOWN | 0.66 | 0.81 | 1.26 |
| 11-13 02:00 | +10 | ZEC | DOWN | 0.67 | 0.78 | 0.80 |
| 11-13 02:00 | +5 | ZEC | DOWN | 0.65 | 0.72 | 0.39 |
| 11-13 02:00 | +10 stop | XRP | DOWN | 0.63 | 0.76 | 1.00 |
| 11-13 02:00 | +20 | XRP | DOWN | 0.63 | 0.85 | 1.94 |
| 11-13 02:00 | +15 | XRP | DOWN | 0.63 | 0.78 | 1.20 |
| 11-13 02:00 | +10 | XRP | DOWN | 0.63 | 0.76 | 1.00 |
| 11-13 02:00 | +5 | XRP | DOWN | 0.63 | 0.76 | 1.00 |
| 11-13 01:56 | +5 | HYPE | DOWN | 0.59 | yes | -6.07 |
| 11-13 01:56 | +10 stop | BTC | DOWN | 0.63 | 0.43 | -2.35 |
| 11-13 01:56 | +10 stop | ZEC | DOWN | 0.50 | 0.65 | 1.16 |
| 11-13 01:56 | +10 | ZEC | DOWN | 0.50 | 0.65 | 1.16 |
| 11-13 01:56 | +5 | ZEC | DOWN | 0.50 | 0.65 | 1.16 |
| 11-13 01:56 | +5 | HYPE | UP | 0.44 | 0.58 | 1.04 |
| 11-13 01:55 | +10 stop | ETH | DOWN | 0.54 | 0.27 | -3.02 |
| 11-13 01:54 | +10 stop | BTC | DOWN | 0.58 | 0.69 | 0.77 |
| 11-13 01:54 | +10 stop | DOGE | UP | 0.62 | 0.72 | 0.68 |
