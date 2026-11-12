# Range-Scalp Bot

*Updated Thu Nov 12 23:34 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 57457 | 50104 | 7353 (101) | 6 | $-15695.60 | -4.3% |
| **+10¢** | 42947 | 34362 | 8585 (133) | 7 | $-14631.55 | -5.4% |
| **+15¢** | 36007 | 26768 | 9239 (167) | 8 | $-13192.96 | -5.8% |
| **+20¢** | 32082 | 22389 | 9693 (217) | 8 | $-11539.30 | -5.7% |
| **+10¢ (15¢ stop)** | 70065 | 69937 | 128 (78) | 7 | $-25835.93 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-12 23:34 | +10 stop | ZEC | DOWN | 0.62 | open |  |
| 11-12 23:33 | +10 stop | ETH | DOWN | 0.56 | open |  |
| 11-12 23:33 | +5 | NEAR | DOWN | 0.63 | open |  |
| 11-12 23:33 | +10 stop | DOGE | DOWN | 0.46 | open |  |
| 11-12 23:33 | +10 stop | NEAR | DOWN | 0.58 | open |  |
| 11-12 23:33 | +10 | NEAR | DOWN | 0.58 | open |  |
| 11-12 23:33 | +5 | NEAR | DOWN | 0.58 | 0.66 | 0.46 |
| 11-12 23:32 | +10 stop | NEAR | DOWN | 0.55 | 0.66 | 0.76 |
| 11-12 23:32 | +20 | NEAR | DOWN | 0.55 | open |  |
| 11-12 23:32 | +15 | NEAR | DOWN | 0.55 | open |  |
| 11-12 23:32 | +10 | NEAR | DOWN | 0.55 | 0.66 | 0.76 |
| 11-12 23:32 | +5 | NEAR | DOWN | 0.55 | 0.66 | 0.76 |
| 11-12 23:31 | +5 | SOL | UP | 0.65 | open |  |
| 11-12 23:31 | +10 stop | ZEC | UP | 0.54 | 0.39 | -1.85 |
| 11-12 23:31 | +20 | ZEC | UP | 0.54 | open |  |
| 11-12 23:31 | +15 | ZEC | UP | 0.53 | open |  |
| 11-12 23:31 | +10 | ZEC | UP | 0.53 | open |  |
| 11-12 23:31 | +5 | BTC | UP | 0.68 | open |  |
| 11-12 23:31 | +10 stop | ETH | UP | 0.67 | 0.49 | -2.14 |
| 11-12 23:31 | +20 | ETH | UP | 0.66 | open |  |
| 11-12 23:31 | +15 | ETH | UP | 0.67 | open |  |
| 11-12 23:31 | +10 | ETH | UP | 0.67 | open |  |
| 11-12 23:31 | +5 | ETH | UP | 0.67 | open |  |
| 11-12 23:31 | +10 stop | DOGE | UP | 0.59 | 0.44 | -1.85 |
| 11-12 23:31 | +20 | DOGE | UP | 0.58 | open |  |
| 11-12 23:31 | +15 | DOGE | UP | 0.58 | open |  |
| 11-12 23:31 | +10 | DOGE | UP | 0.58 | open |  |
| 11-12 23:31 | +5 | DOGE | UP | 0.58 | open |  |
| 11-12 23:31 | +5 | ZEC | UP | 0.71 | open |  |
| 11-12 23:30 | +10 stop | BTC | UP | 0.60 | open |  |
| 11-12 23:30 | +20 | BTC | UP | 0.60 | open |  |
| 11-12 23:30 | +15 | BTC | UP | 0.60 | open |  |
| 11-12 23:30 | +10 | BTC | UP | 0.60 | open |  |
| 11-12 23:30 | +5 | BTC | UP | 0.59 | 0.64 | 0.16 |
| 11-12 23:30 | +10 stop | BNB | UP | 0.68 | open |  |
| 11-12 23:30 | +20 | BNB | UP | 0.68 | open |  |
| 11-12 23:30 | +15 | BNB | UP | 0.68 | open |  |
| 11-12 23:30 | +10 | BNB | UP | 0.69 | open |  |
| 11-12 23:30 | +5 | BNB | UP | 0.70 | 0.75 | 0.21 |
| 11-12 23:30 | +10 stop | SOL | UP | 0.60 | open |  |
