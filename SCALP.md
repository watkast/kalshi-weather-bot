# Range-Scalp Bot

*Updated Tue Nov 10 00:12 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 54069 | 47163 | 6906 (89) | 1 | $-14746.82 | -4.3% |
| **+10¢** | 40386 | 32328 | 8058 (117) | 2 | $-13712.29 | -5.4% |
| **+15¢** | 33848 | 25163 | 8685 (149) | 3 | $-12481.50 | -5.9% |
| **+20¢** | 30135 | 21026 | 9109 (195) | 3 | $-10916.58 | -5.8% |
| **+10¢ (15¢ stop)** | 65868 | 65758 | 110 (66) | 0 | $-24372.53 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-10 00:11 | +5 | NEAR | DOWN | 0.69 | 0.83 | 1.15 |
| 11-10 00:11 | +10 stop | BTC | UP | 0.58 | 0.43 | -1.86 |
| 11-10 00:11 | +10 stop | NEAR | UP | 0.46 | 0.16 | -3.32 |
| 11-10 00:11 | +20 | NEAR | UP | 0.46 | open |  |
| 11-10 00:11 | +15 | NEAR | UP | 0.46 | open |  |
| 11-10 00:11 | +10 | NEAR | UP | 0.46 | open |  |
| 11-10 00:11 | +5 | NEAR | UP | 0.46 | 0.53 | 0.30 |
| 11-10 00:10 | +10 stop | DOGE | DOWN | 0.65 | 0.80 | 1.22 |
| 11-10 00:10 | +10 stop | ETH | UP | 0.60 | 0.43 | -2.05 |
| 11-10 00:09 | +10 stop | DOGE | UP | 0.68 | 0.46 | -2.54 |
| 11-10 00:09 | +15 | DOGE | UP | 0.67 | open |  |
| 11-10 00:09 | +5 | DOGE | UP | 0.67 | open |  |
| 11-10 00:08 | +10 stop | ETH | UP | 0.64 | 0.75 | 0.79 |
| 11-10 00:08 | +10 stop | SOL | UP | 0.70 | 0.80 | 0.73 |
| 11-10 00:06 | +10 stop | DOGE | DOWN | 0.47 | 0.30 | -2.03 |
| 11-10 00:06 | +10 stop | HYPE | DOWN | 0.51 | 0.26 | -2.82 |
| 11-10 00:06 | +10 stop | NEAR | UP | 0.52 | 0.83 | 2.82 |
| 11-10 00:06 | +10 stop | BTC | UP | 0.52 | 0.63 | 0.75 |
| 11-10 00:06 | +10 stop | DOGE | UP | 0.57 | 0.41 | -1.95 |
| 11-10 00:05 | +10 stop | SOL | DOWN | 0.58 | 0.37 | -2.45 |
| 11-10 00:05 | +10 stop | ETH | DOWN | 0.67 | 0.42 | -2.84 |
| 11-10 00:05 | +15 | ETH | DOWN | 0.67 | 0.85 | 1.55 |
| 11-10 00:05 | +10 | ETH | DOWN | 0.66 | 0.85 | 1.65 |
| 11-10 00:05 | +5 | ETH | DOWN | 0.66 | 0.85 | 1.65 |
| 11-10 00:04 | +10 stop | DOGE | DOWN | 0.61 | 0.45 | -1.95 |
| 11-10 00:04 | +10 stop | HYPE | UP | 0.67 | 0.41 | -2.93 |
| 11-10 00:04 | +20 | HYPE | UP | 0.67 | 0.91 | 2.12 |
| 11-10 00:04 | +15 | HYPE | UP | 0.67 | 0.85 | 1.55 |
| 11-10 00:04 | +10 | HYPE | UP | 0.67 | 0.80 | 1.02 |
| 11-10 00:04 | +5 | HYPE | UP | 0.67 | 0.72 | 0.19 |
| 11-10 00:04 | +10 stop | NEAR | UP | 0.61 | 0.46 | -1.88 |
| 11-10 00:04 | +10 | NEAR | UP | 0.62 | 0.83 | 1.87 |
| 11-10 00:03 | +10 stop | SOL | UP | 0.59 | 0.44 | -1.85 |
| 11-10 00:03 | +10 | SOL | UP | 0.59 | 0.69 | 0.68 |
| 11-10 00:03 | +5 | SOL | UP | 0.65 | 0.79 | 1.12 |
| 11-10 00:03 | +10 stop | DOGE | UP | 0.67 | 0.50 | -2.04 |
| 11-10 00:03 | +10 | DOGE | UP | 0.67 | open |  |
| 11-10 00:03 | +5 | DOGE | UP | 0.67 | 0.74 | 0.40 |
| 11-10 00:02 | +5 | NEAR | UP | 0.70 | 0.83 | 1.05 |
| 11-10 00:02 | +5 | DOGE | UP | 0.60 | 0.67 | 0.37 |
